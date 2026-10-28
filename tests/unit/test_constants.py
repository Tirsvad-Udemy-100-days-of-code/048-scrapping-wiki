"""Tests of the constants: they are the one place that names the page and the selector."""

from scraping_wiki import constants


def test_url_is_the_wikipedia_main_page() -> None:
    assert constants.WIKIPEDIA_MAIN_PAGE_URL == "https://en.wikipedia.org/wiki/Main_Page"


def test_lecture_selector_targets_the_first_anchor_in_the_article_count_div() -> None:
    assert constants.LECTURE_SELECTOR == "#articlecount a"


def test_article_count_selector_targets_the_link_of_the_second_list_item() -> None:
    assert constants.ARTICLE_COUNT_SELECTOR == "#articlecount li:nth-of-type(2) a"
