from playwright.sync_api import sync_playwright
from creds import EMAIL, PASSWORD


with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False, slow_mo=5000)
    # page = browser.new_page()
    # page.set_viewport_size({"width":922, "height":950})
    #
    # page.goto("https://accounts.google.com/")
    #
    # email_input = page.get_by_label("Email or phone")
    # email_input.fill(EMAIL)
    # next_btn = page.get_by_role("button", name="Next")
    # next_btn.click()
    #
    # password_input = page.get_by_label("Enter your password")
    # password_input.fill(PASSWORD)
    # next_btn = page.get_by_role("button", name="Next")
    # next_btn.click()

    # ___________________Save Authinication State_________________________
    # context = browser.new_context()
    #
    # page = context.new_page()
    # page.goto("https://accounts.google.com/")
    #
    # # Enter email
    # email_input = page.get_by_label("Email or phone")
    # email_input.fill(EMAIL)
    #
    # next_btn = page.get_by_role("button", name="Next")
    # next_btn.click()
    #
    # # Enter password
    # password_input = page.get_by_label("Enter your password")
    # password_input.fill(PASSWORD)
    #
    # next_btn = page.get_by_role("button", name="Next")
    # next_btn.click()
    #
    # page.pause()
    #
    # # save authentication state
    # context.storage_state(path="playwright/.auth/storage_state.json")
    #
    # context.close()

    # ___________________Reuse Authinication State_________________________
    context = browser.new_context(storage_state="playwright/.auth/storage_state.json")

    page = context.new_page()
    page.goto("https://accounts.google.com/")

    page.pause()

    context.close()
