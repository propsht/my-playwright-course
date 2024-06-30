import pytest
from playwright.sync_api import Page, Browser, BrowserContext

DOCS_URL = "https://playwright.dev/python/docs/intro"

@pytest.fixture
def recording_page(browser: Browser):
    context = browser.new_context(
        record_video_dir="video/"
    )
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(autouse=True, scope="function")
def visit_playwright(page: Page):
    page.goto("https://playwright.dev/python/")

    yield page
    page.close()

@pytest.fixture(autouse=True)
def trace_test(context:BrowserContext):
    #setup hook
    context.tracing.start(
        name="playwright",
        screenshots=True,
        snapshots=True,
        sources=True,
    )
    yield
    context.tracing.stop(path="trace/trace.zip")
    #playwright show-trace trace/trace.zip



def test_page_has_doc_link(page: Page):

    link = page.get_by_role("link", name="Docs")

    assert link.is_visible()


def test_page_has_get_started_link(page: Page):

    link = page.get_by_role("link", name="Get started")
    link.screenshot(path="screenshot/get_started_link.png")
    link.click()
    page.screenshot(path="screenshot/playwright.png", full_page=True)
    assert page.url == DOCS_URL

def test_page_has_get_started_link_video(recording_page: Page):
    recording_page.goto("https://playwright.dev/python/")
    theme_btn= recording_page.get_by_title("Switch between dark and light mode (currently dark mode)")
    recording_page.wait_for_timeout(1000)
    theme_btn.click()
    recording_page.wait_for_timeout(1000)

    link = recording_page.get_by_role("link", name="Get started")
    link.screenshot(path="screenshot/get_started_link.png")
    link.click()
    recording_page.screenshot(path="screenshot/playwright.png", full_page=True)
    assert recording_page.url == DOCS_URL


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
