from playwright.sync_api import Page, expect

DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="GET STARTED")
    expect(link).to_be_visible()
    expect(link).to_be_enabled()
    expect(link).not_to_be_hidden()
    link.click()

    # assert page.url == DOCS_URL
    expect(page).to_have_url(DOCS_URL)
    expect(page).to_have_title("Installation | Playwright Python")
