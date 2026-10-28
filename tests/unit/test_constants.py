"""Tests of the constants: they are the one place that names the page and the selector."""

from scraping_wiki import constants


def test_url_is_the_wikipedia_main_page() -> None:
    assert constants.WIKIPEDIA_MAIN_PAGE_URL == "https://en.wikipedia.org/wiki/Main_Page"


def test_selector_targets_the_anchor_in_the_article_count_div() -> None:
    assert constants.ARTICLE_COUNT_SELECTOR == "#articlecount a"
