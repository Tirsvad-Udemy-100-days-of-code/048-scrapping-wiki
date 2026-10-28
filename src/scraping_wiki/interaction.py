"""@file
@brief The lecture script: open the Wikipedia main page and print the article count.

Run it with `python -m scraping_wiki.interaction`, or add `--headless` to run
without a browser window (as the Docker run does).
"""

import argparse
import os
from collections.abc import Sequence

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from scraping_wiki.constants import (
    ARTICLE_COUNT_SELECTOR,
    CHROME_BINARY_ENV,
    CHROMEDRIVER_PATH_ENV,
    DISABLE_SHM_ARGUMENT,
    HEADLESS_ARGUMENT,
    HEADLESS_FLAG,
    NO_SANDBOX_ARGUMENT,
    WIKIPEDIA_MAIN_PAGE_URL,
    WINDOW_SIZE_ARGUMENT,
)


def create_driver(headless: bool = False) -> WebDriver:
    """@brief Initialise the Chrome driver.

    @param headless True to run Chrome without a window and with the options a container needs.
    @return The Chrome driver that controls the browser.
    """
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument(HEADLESS_ARGUMENT)
        options.add_argument(NO_SANDBOX_ARGUMENT)
        options.add_argument(DISABLE_SHM_ARGUMENT)
        options.add_argument(WINDOW_SIZE_ARGUMENT)
    binary = os.environ.get(CHROME_BINARY_ENV)
    if binary:
        options.binary_location = binary
    driver_path = os.environ.get(CHROMEDRIVER_PATH_ENV)
    service = Service(executable_path=driver_path) if driver_path else Service()
    return webdriver.Chrome(options=options, service=service)


def open_main_page(driver: WebDriver) -> None:
    """@brief Navigate to the Wikipedia main page with `get()`.

    @param driver The driver that controls the browser.
    """
    driver.get(WIKIPEDIA_MAIN_PAGE_URL)


def read_article_count(driver: WebDriver) -> str:
    """@brief Find the article count link (first link of the second list item) and return its text.

    @param driver A driver that has the Wikipedia main page open.
    @return The text of the first link of the second list item in the `articlecount` div,
        for example `7,000,000`.
    """
    article_count = driver.find_element(By.CSS_SELECTOR, ARTICLE_COUNT_SELECTOR)
    return article_count.text


def main(argv: Sequence[str] | None = None) -> int:
    """@brief Open the main page, print the article count and close the browser.

    @param argv Command line arguments; `--headless` runs without a browser window.
    @return The exit code, 0 when the count was printed.
    """
    parser = argparse.ArgumentParser(description="Print the Wikipedia article count.")
    parser.add_argument(
        HEADLESS_FLAG,
        action="store_true",
        help="run Chrome without a window",
    )
    arguments = parser.parse_args(argv)
    driver = create_driver(headless=arguments.headless)
    try:
        open_main_page(driver)
        print(read_article_count(driver))
    finally:
        driver.quit()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
