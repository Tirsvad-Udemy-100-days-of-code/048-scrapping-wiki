"""@file
@brief Constants of the Wikipedia scraper: the page, the selector and the Chrome options.
"""

## @brief The Wikipedia main page that the scraper opens.
WIKIPEDIA_MAIN_PAGE_URL: str = "https://en.wikipedia.org/wiki/Main_Page"

## @brief The CSS selector shown in the lecture. It matched the article count when the lecture
# was recorded; today it matches the first link, the active editors.
LECTURE_SELECTOR: str = "#articlecount a"

## @brief CSS selector of the article count link: the first anchor of the second list item
# inside the div whose id is `articlecount`.
ARTICLE_COUNT_SELECTOR: str = "#articlecount li:nth-of-type(2) a"

## @brief Chrome option that runs the browser without a window.
HEADLESS_ARGUMENT: str = "--headless=new"

## @brief Chrome option needed when Chromium runs as a user inside a container.
NO_SANDBOX_ARGUMENT: str = "--no-sandbox"

## @brief Chrome option that keeps Chromium from using the small shared memory of a container.
DISABLE_SHM_ARGUMENT: str = "--disable-dev-shm-usage"

## @brief Chrome option that gives a headless run a window size, so screenshots are readable.
WINDOW_SIZE_ARGUMENT: str = "--window-size=1280,1000"

## @brief Environment variable that names the Chrome or Chromium binary to use (optional).
CHROME_BINARY_ENV: str = "CHROME_BINARY"

## @brief Environment variable that names the chromedriver binary to use (optional).
CHROMEDRIVER_PATH_ENV: str = "CHROMEDRIVER_PATH"

## @brief Name of the command line flag that starts the scraper without a browser window.
HEADLESS_FLAG: str = "--headless"
