"""@file
@brief Capture one screenshot per lecture step with headless Chromium.

Usage: `python tests/e2e/capture_screenshots.py <output_dir>`. Runs only inside the Docker
container (see tests/e2e/run_e2e.sh), never on the host desktop.
"""

import html
import re
import sys
from collections.abc import Sequence
from pathlib import Path
from tempfile import TemporaryDirectory

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from scraping_wiki.constants import (
    ARTICLE_COUNT_SELECTOR,
    LECTURE_SELECTOR,
    WIKIPEDIA_MAIN_PAGE_URL,
)
from scraping_wiki.interaction import create_driver, open_main_page, read_article_count

## @brief Folder with the lecture step scripts, relative to the repository root.
LECTURE_STEPS_FOLDER: Path = Path("docs") / "lecture-steps"

## @brief The repository root, two folders above this file (tests/e2e/).
REPOSITORY_ROOT: Path = Path(__file__).resolve().parents[2]

## @brief Step number, file name prefix of the lecture script, screenshot name and title.
STEPS: dict[int, tuple[str, str, str]] = {
    1: ("step_1_", "step-1-create-the-file.png", "Create the file"),
    2: ("step_2_", "step-2-import-selenium.png", "Import Selenium"),
    3: ("step_3_", "step-3-initialise-chrome-driver.png", "Initialise the Chrome driver"),
    4: ("step_4_", "step-4-navigate-with-get.png", "Navigate with get()"),
    5: ("step_5_", "step-5-identify-the-element.png", "Identify the element"),
    6: ("step_6_", "step-6-find-element-and-print.png", "Find the element and print its text"),
    7: ("step_7_", "step-7-future-interactions.png", "Future interactions"),
}

## @brief Title of the editor window in the rendered source pages.
EDITOR_FILE_NAME: str = "interaction.py"

## @brief The command shown in the terminal panel of step 6.
TERMINAL_COMMAND: str = "$ python interaction.py"

## @brief Pattern the article count text must match.
ARTICLE_COUNT_PATTERN: str = r"^[\d,]+$"

## @brief CSS selector of the Wikipedia search field, and its fallback.
SEARCH_SELECTOR: str = 'input[name="search"]'
SEARCH_FALLBACK_SELECTOR: str = 'input[type="search"]'

## @brief Banner texts of the steps that annotate the real Wikipedia page.
STEP_4_BANNER: str = f'Step 4: driver.get("{WIKIPEDIA_MAIN_PAGE_URL}")'
STEP_5_BANNER: str = (
    f"Step 5: {LECTURE_SELECTOR} (red). "
    f"Today the articles link is the 2nd: {ARTICLE_COUNT_SELECTOR} (green)"
)
STEP_7_BANNER: str = "Step 7: next lectures: click links and type into search fields"

## @brief Style of the highlighted elements: the lecture selector red, the article link green.
LECTURE_HIGHLIGHT_COLOR: str = "red"
ARTICLE_HIGHLIGHT_COLOR: str = "green"
HIGHLIGHT_WIDTH: str = "4px solid "
HIGHLIGHT_BACKGROUND: str = "lightyellow"

## @brief Second line of the terminal panel in step 6, before the real article count.
TODAYS_COUNT_PREFIX: str = "# today's article count: "

## @brief Style of the banner at the bottom of the Wikipedia page; long text wraps.
BANNER_STYLE: str = (
    "position:fixed;bottom:0;left:0;right:0;white-space:normal;word-wrap:break-word;"
    "z-index:2147483647;padding:12px 20px;"
    "background:#1e1e1e;color:#fff;font:bold 20px 'DejaVu Sans Mono',monospace;"
)

## @brief Style sheet shared by the rendered source pages.
PAGE_STYLE: str = """
body { margin: 0; background: #1e1e1e; color: #d4d4d4;
       font: 20px/1.5 'DejaVu Sans Mono', monospace; }
.title-bar { background: #333; color: #fff; padding: 8px 16px; font-size: 18px; }
h1 { margin: 16px; font-size: 28px; color: #4ec9b0; }
.layout { display: flex; }
.editor { flex: 1; padding: 0 16px; }
.terminal { flex: 1; margin: 0 16px; padding: 16px; background: #000; color: #0f0;
            min-height: 200px; }
.line { white-space: pre; }
.number { display: inline-block; width: 3em; color: #858585; text-align: right;
          margin-right: 1.5em; }
"""

## @brief Seconds to wait until the images in the first view are loaded.
IMAGE_WAIT_SECONDS: int = 15

## @brief Where a scrolled element lands in the window.
SCROLL_ELEMENT_BLOCK: str = "center"


def find_step_source(step_number: int) -> str:
    """@brief Read the lecture script of one step.

    @param step_number The step, 1 to 7.
    @return The source text of docs/lecture-steps/step_N_*.py.
    @raises FileNotFoundError When the script of the step does not exist.
    """
    prefix = STEPS[step_number][0]
    folder = REPOSITORY_ROOT / LECTURE_STEPS_FOLDER
    matches = sorted(folder.glob(f"{prefix}*.py"))
    if not matches:
        raise FileNotFoundError(f"No lecture script {prefix}*.py in {folder}")
    return matches[0].read_text(encoding="utf-8")


def render_source_lines(source: str) -> str:
    """@brief Render source text as numbered, HTML-escaped lines.

    @param source The source text.
    @return HTML of the lines, each with its line number.
    """
    lines = source.rstrip("\n").split("\n")
    return "".join(
        f'<div class="line"><span class="number">{number}</span>{html.escape(line)}</div>'
        for number, line in enumerate(lines, start=1)
    )


def render_page(step_number: int, source: str, terminal_text: str | None = None) -> str:
    """@brief Render the source of a step as an editor-style HTML page.

    @param step_number The step, 1 to 7.
    @param source The source text of the step.
    @param terminal_text When given, a terminal panel with this text is shown on the right.
    @return The HTML page.
    """
    title = STEPS[step_number][2]
    terminal = ""
    if terminal_text is not None:
        terminal_lines = "<br>".join(html.escape(line) for line in terminal_text.split("\n"))
        terminal = f'<div class="terminal">{terminal_lines}</div>'
    return (
        f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{PAGE_STYLE}</style></head>"
        f"<body><div class='title-bar'>{html.escape(EDITOR_FILE_NAME)}</div>"
        f"<h1>Step {step_number}: {html.escape(title)}</h1>"
        f"<div class='layout'><div class='editor'>{render_source_lines(source)}</div>"
        f"{terminal}</div></body></html>"
    )


def screenshot_html(driver: WebDriver, page: str, target: Path) -> None:
    """@brief Load an HTML page from a temporary file and save a screenshot of it.

    @param driver The driver that controls the browser.
    @param page The HTML page.
    @param target The PNG file to write.
    """
    with TemporaryDirectory() as folder:
        page_file = Path(folder) / "page.html"
        page_file.write_text(page, encoding="utf-8", newline="\n")
        driver.get(page_file.as_uri())
        save_screenshot(driver, target)


def save_screenshot(driver: WebDriver, target: Path) -> None:
    """@brief Save the current view of the browser as a PNG and report it.

    @param driver The driver that controls the browser.
    @param target The PNG file to write.
    @raises RuntimeError When the browser cannot save the file.
    """
    if not driver.save_screenshot(str(target)):
        raise RuntimeError(f"Could not save screenshot {target}")
    print(f"saved {target}")


def add_banner(driver: WebDriver, text: str) -> None:
    """@brief Show a fixed banner at the bottom of the current page.

    @param driver The driver that controls the browser.
    @param text The banner text.
    """
    driver.execute_script(
        "const b = document.createElement('div'); b.textContent = arguments[0];"
        "b.style.cssText = arguments[1]; document.body.appendChild(b);",
        text,
        BANNER_STYLE,
    )


def highlight(driver: WebDriver, element: WebElement, color: str) -> None:
    """@brief Outline an element in a colour on a light yellow background.

    @param driver The driver that controls the browser.
    @param element The element to highlight.
    @param color The outline colour.
    """
    driver.execute_script(
        "arguments[0].style.outline = arguments[1]; arguments[0].style.background = arguments[2];",
        element,
        HIGHLIGHT_WIDTH + color,
        HIGHLIGHT_BACKGROUND,
    )


def scroll_to_center(driver: WebDriver, element: WebElement) -> None:
    """@brief Scroll an element to the middle of the window, clear of the banner.

    @param driver The driver that controls the browser.
    @param element The element to show.
    """
    driver.execute_script(
        "arguments[0].scrollIntoView({block: arguments[1]});", element, SCROLL_ELEMENT_BLOCK
    )


def find_required(driver: WebDriver, selector: str) -> WebElement:
    """@brief Find an element by CSS selector.

    @param driver The driver that controls the browser.
    @param selector The CSS selector.
    @return The element.
    @raises LookupError When the selector finds nothing.
    """
    elements = driver.find_elements(By.CSS_SELECTOR, selector)
    if not elements:
        raise LookupError(f"Selector {selector!r} found nothing on {driver.current_url}")
    return elements[0]


def find_search_field(driver: WebDriver) -> WebElement:
    """@brief Find the Wikipedia search input, with a fallback to any search input.

    @param driver The driver that controls the browser.
    @return The search input.
    @raises LookupError When neither selector finds an element.
    """
    for selector in (SEARCH_SELECTOR, SEARCH_FALLBACK_SELECTOR):
        elements = driver.find_elements(By.CSS_SELECTOR, selector)
        if elements:
            return elements[0]
    raise LookupError(f"Neither {SEARCH_SELECTOR!r} nor {SEARCH_FALLBACK_SELECTOR!r} found")


def read_checked_article_count(driver: WebDriver) -> str:
    """@brief Read the article count and check that it looks like a number.

    @param driver A driver that has the Wikipedia main page open.
    @return The article count text.
    @raises LookupError When the text does not match the number pattern.
    """
    find_required(driver, ARTICLE_COUNT_SELECTOR)
    count = read_article_count(driver)
    if not re.fullmatch(ARTICLE_COUNT_PATTERN, count):
        raise LookupError(f"Article count {count!r} does not match {ARTICLE_COUNT_PATTERN!r}")
    return count


def open_loaded_main_page(driver: WebDriver) -> None:
    """@brief Open the main page and wait until the images in the first view are loaded.

    @param driver The driver that controls the browser.
    @raises selenium.common.exceptions.TimeoutException When the images do not load in time.
    """
    open_main_page(driver)
    WebDriverWait(driver, IMAGE_WAIT_SECONDS).until(
        lambda d: d.execute_script(
            "return Array.from(document.images)"
            ".filter(i => i.getBoundingClientRect().top < window.innerHeight)"
            ".every(i => i.complete);"
        )
    )


def capture_source_steps(driver: WebDriver, output: Path) -> None:
    """@brief Capture steps 1 to 3: the source of the step in an editor-style page.

    @param driver The driver that controls the browser.
    @param output The folder for the PNG files.
    """
    for step_number in (1, 2, 3):
        page = render_page(step_number, find_step_source(step_number))
        screenshot_html(driver, page, output / STEPS[step_number][1])


def capture_page_steps(driver: WebDriver, output: Path) -> None:
    """@brief Capture steps 4, 5 and 7: the real Wikipedia page with a banner.

    @param driver The driver that controls the browser.
    @param output The folder for the PNG files.
    """
    open_loaded_main_page(driver)
    add_banner(driver, STEP_4_BANNER)
    save_screenshot(driver, output / STEPS[4][1])

    open_loaded_main_page(driver)
    lecture_match = find_required(driver, LECTURE_SELECTOR)
    article_count = find_required(driver, ARTICLE_COUNT_SELECTOR)
    scroll_to_center(driver, article_count)
    highlight(driver, lecture_match, LECTURE_HIGHLIGHT_COLOR)
    highlight(driver, article_count, ARTICLE_HIGHLIGHT_COLOR)
    add_banner(driver, STEP_5_BANNER)
    save_screenshot(driver, output / STEPS[5][1])

    open_loaded_main_page(driver)
    article_count = find_required(driver, ARTICLE_COUNT_SELECTOR)
    search = find_search_field(driver)
    # The input's own outline is clipped by its wrapper, so outline the wrapper.
    highlight(driver, search.find_element(By.XPATH, ".."), LECTURE_HIGHLIGHT_COLOR)
    highlight(driver, article_count, ARTICLE_HIGHLIGHT_COLOR)
    driver.execute_script("window.scrollTo(0, 0);")
    add_banner(driver, STEP_7_BANNER)
    save_screenshot(driver, output / STEPS[7][1])


def capture_print_step(driver: WebDriver, output: Path) -> None:
    """@brief Capture step 6: the source and a terminal with the real article count.

    @param driver The driver that controls the browser.
    @param output The folder for the PNG files.
    """
    open_main_page(driver)
    count = read_checked_article_count(driver)
    lecture_text = find_required(driver, LECTURE_SELECTOR).text
    terminal_text = f"{TERMINAL_COMMAND}\n{lecture_text}\n{TODAYS_COUNT_PREFIX}{count}"
    page = render_page(6, find_step_source(6), terminal_text)
    screenshot_html(driver, page, output / STEPS[6][1])


def main(argv: Sequence[str] | None = None) -> int:
    """@brief Capture the seven screenshots into a folder.

    @param argv Command line arguments: the output folder.
    @return The exit code, 0 when all seven files were saved, 2 for a usage error.
    """
    arguments = list(sys.argv[1:] if argv is None else argv)
    if len(arguments) != 1:
        print("usage: capture_screenshots.py <output_dir>", file=sys.stderr)
        return 2
    output = Path(arguments[0])
    output.mkdir(parents=True, exist_ok=True)
    driver = create_driver(headless=True)
    try:
        capture_source_steps(driver, output)
        capture_page_steps(driver, output)
        capture_print_step(driver, output)
    finally:
        driver.quit()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
