from playwright.sync_api import sync_playwright
from creds import EMAIL_QUORA, PASSWORD_QUORA


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=5000)
    # ___________________Save Authinication State_________________________
    # context = browser.new_context()
    #
    # page = context.new_page()
    # page.goto("https://www.quora.com/")
    #
    # # Enter email
    # email_input = page.get_by_label("Email")
    # email_input.fill(EMAIL_QUORA)
    # # Enter password
    # password_input = page.get_by_label("Password")
    # password_input.fill(PASSWORD_QUORA)
    #
    # next_btn = page.get_by_role("button", name="Login")
    # next_btn.click()
    #
    # page.pause()
    #
    # # save authentication state
    # context.storage_state(path="playwright/.auth/quora_state.json")
    #
    # context.close()

    # ___________________Reuse Authinication State_________________________
    context = browser.new_context(storage_state="playwright/.auth/quora_state.json")

    page = context.new_page()
    page.goto("https://qr.ae/psB6nc")
    upvote_btn = page.get_by_text("Upvote")
    upvote_btn[1].click()

    page.pause()

    context.close()
