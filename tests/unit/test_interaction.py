"""Tests of the lecture script. A fake driver stands in for Chrome, so no browser starts."""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from scraping_wiki import interaction
from scraping_wiki.constants import (
    ARTICLE_COUNT_SELECTOR,
    CHROME_BINARY_ENV,
    CHROMEDRIVER_PATH_ENV,
    HEADLESS_ARGUMENT,
    WIKIPEDIA_MAIN_PAGE_URL,
)


class FakeElement:
    def __init__(self, text: str) -> None:
        self.text = text


class FakeDriver:
    def __init__(self, count: str = "7,123,456") -> None:
        self.count = count
        self.visited: list[str] = []
        self.searched: list[tuple[str, str]] = []
        self.is_quit = False

    def get(self, url: str) -> None:
        self.visited.append(url)

    def find_element(self, by: str, value: str) -> FakeElement:
        self.searched.append((by, value))
        return FakeElement(self.count)

    def quit(self) -> None:
        self.is_quit = True


class RecordingChrome:
    def __init__(self, options: object, service: object) -> None:
        self.options = options
        self.service = service


def test_open_main_page_gets_the_wikipedia_url() -> None:
    driver = FakeDriver()
    interaction.open_main_page(driver)  # type: ignore[arg-type]
    assert driver.visited == [WIKIPEDIA_MAIN_PAGE_URL]


def test_read_article_count_uses_the_css_selector_and_returns_the_text() -> None:
    driver = FakeDriver("7,000,001")
    assert interaction.read_article_count(driver) == "7,000,001"  # type: ignore[arg-type]
    assert driver.searched == [(By.CSS_SELECTOR, ARTICLE_COUNT_SELECTOR)]


def test_main_prints_the_count_and_quits_the_driver(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    driver = FakeDriver("6,999,999")
    monkeypatch.setattr(interaction, "create_driver", lambda headless=False: driver)
    assert interaction.main([]) == 0
    assert capsys.readouterr().out == "6,999,999\n"
    assert driver.visited == [WIKIPEDIA_MAIN_PAGE_URL]
    assert driver.is_quit


def test_main_quits_the_driver_when_reading_fails(monkeypatch: pytest.MonkeyPatch) -> None:
    driver = FakeDriver()

    def fail(_driver: object) -> str:
        raise RuntimeError("element not found")

    monkeypatch.setattr(interaction, "create_driver", lambda headless=False: driver)
    monkeypatch.setattr(interaction, "read_article_count", fail)
    with pytest.raises(RuntimeError):
        interaction.main([])
    assert driver.is_quit


def test_main_passes_the_headless_flag_to_create_driver(monkeypatch: pytest.MonkeyPatch) -> None:
    seen: list[bool] = []

    def fake_create(headless: bool = False) -> FakeDriver:
        seen.append(headless)
        return FakeDriver()

    monkeypatch.setattr(interaction, "create_driver", fake_create)
    interaction.main(["--headless"])
    interaction.main([])
    assert seen == [True, False]


def test_create_driver_adds_the_headless_options_only_when_asked(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv(CHROME_BINARY_ENV, raising=False)
    monkeypatch.delenv(CHROMEDRIVER_PATH_ENV, raising=False)
    monkeypatch.setattr(
        webdriver, "Chrome", lambda options, service: RecordingChrome(options, service)
    )
    plain = interaction.create_driver()
    headless = interaction.create_driver(headless=True)
    assert HEADLESS_ARGUMENT not in plain.options.arguments  # type: ignore[attr-defined]
    assert HEADLESS_ARGUMENT in headless.options.arguments  # type: ignore[attr-defined]


def test_create_driver_uses_the_binaries_named_in_the_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(CHROME_BINARY_ENV, "/usr/bin/chromium")
    monkeypatch.setenv(CHROMEDRIVER_PATH_ENV, "/usr/bin/chromedriver")
    monkeypatch.setattr(
        webdriver, "Chrome", lambda options, service: RecordingChrome(options, service)
    )
    driver = interaction.create_driver()
    assert driver.options.binary_location == "/usr/bin/chromium"  # type: ignore[attr-defined]
    assert driver.service.path == "/usr/bin/chromedriver"  # type: ignore[attr-defined]
