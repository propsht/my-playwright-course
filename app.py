from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.firefox.launch(headless=False, slow_mo=5000)
    # Create a new page
    page = browser.new_page()
    # visit the playwright website
    page.goto("https://playwright.dev/python/")

    # Locate a link element with
    docs_button = page.get_by_role("link", name="Docs")
    docs_button.click()

    #Get the url
    print("Docs:", page.url)

    browser.close()