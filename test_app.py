import pytest
from playwright.sync_api import Page

DOCS_URL = "https://playwright.dev/python/docs/intro"


@pytest.fixture(autouse=True, scope="function")
def visit_playwright(page: Page):
    page.goto("https://playwright.dev/python/")
    yield page
    page.close()


def test_page_has_doc_link(page: Page):

    link = page.get_by_role("link", name="Docs")

    assert link.is_visible()


def test_page_has_get_started_link(page: Page):

    link = page.get_by_role("link", name="Get started")
    link.click()

    assert page.url == DOCS_URL


# @pytest.fixture()
# def playwright_page(page: Page):
#     page.goto("https://playwright.dev/python/")
#     return page
#
#
# def test_page_has_doc_link(playwright_page: Page):
#
#     link = playwright_page.get_by_role("link", name="Docs" )
#
#     assert link.is_visible()
#
# def test_page_has_get_started_link(playwright_page: Page):
#
#     link = playwright_page.get_by_role("link", name="Get started" )
#     link.click()
#
#     assert playwright_page.url == DOCS_URL
