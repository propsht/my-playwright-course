import time

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.firefox.launch(headless=False, slow_mo=5000)
    # Create a new page
    page = browser.new_page()
    # visit the playwright website
    # page.goto("https://playwright.dev/python/")
    #
    # # Locate a link element with
    # docs_button = page.get_by_role("link", name="Get started")
    # docs_button.highlight()
    # docs_button = page.get_by_role("link", name="Docs")
    # docs_button.click()
    #
    #
    # #Get the url
    # print("Docs:", page.url)

    # page.goto("https://bootswatch.com/default/")
    #
    # heading = page.get_by_role("heading", name="Heading 2")
    # heading.highlight()

    # radio_btn =  page.get_by_role("radio", name="Get started")
    # radio_btn.highlight()

    # #Alt Text
    # page.goto("https://unsplash.com/")
    # page.get_by_alt_text("a green cloud floating over a lush green field").click()

    # Title
    # page.goto("https://bootswatch.com/default/")
    # page.get_by_title("attribute").highlight()

    # CSS
    page.goto("https://bootswatch.com/default/")
    # page.locator("css=h1").highlight()
    # page.locator("footer").highlight()

    # CSS class name
    # page.locator("button.btn-outline-primary").highlight()
    # CSS id
    # page.locator("button#btnGroupDrop1").click()
    # Css Attribute/Value
    # page.locator("input[readonly]").highlight()
    # page.locator("input[value='correct value']").highlight()

    # #CSS Selector - Hierarchy
    # page.locator("div.col-lg-4 >div.bs-component > ul.list-group").nth(1).highlight()
    #
    # #CSS Selector - Pseudo Classes
    # page.locator("h1:text('Navbars')").highlight()

    # page.locator("id=btnGroupDrop1").click()
    # page.locator("div.dropdown-menu:visible").highlight()

    # page.locator(":nth-match(button.btn-primary, 5)").highlight()
    # page.locator(":nth-match(button:text('Primary'),2)").highlight()

    # #XPATH
    # page.locator("xpath=//h1[@id='navbars']").highlight()
    # time.sleep(5)
    # ## atribute
    # page.locator("//input[@readonly]").highlight()
    # time.sleep(5)
    # ## value
    # page.locator("//input[@value='wrong value']").highlight()
    # time.sleep(5)
    # ## text
    # page.locator("xpath=//h1[ text() = 'Heading 1']").highlight()
    # time.sleep(5)
    # ## include text
    # page.locator("xpath=//h1[ contains(text(), 'Head')]").highlight()
    # time.sleep(5)
    # page.locator("xpath=//button[contains(@class, 'btn-outline-primary') ]").highlight()
    # time.sleep(5)

    # page.locator("xpath=//input[ contains(@value, 'correct value')]").highlight()

    # Other
    # numeric element
    # page.get_by_role("button", name="Primary").locator("nth=1").highlight()
    # time.sleep(5)
    # page.locator("button").locator("nth=18").highlight()

    # Parent element
    # page.get_by_label("Email address").highlight()
    # time.sleep(5)
    # page.get_by_label("Email address").locator("..").highlight()
    # time.sleep(5)
    #
    #
    # page.locator("id=btnGroupDrop1").highlight()
    # time.sleep(5)
    #
    # page.locator("id=btnGroupDrop1").click()
    # page.locator("div.dropdown-menu").locator("visible=true").highlight()
    #
    # # Element based on Filter
    # page.get_by_role("heading").filter(has_text="Heading").highlight()
    #
    # page.locator("div.bs-component").filter(
    #     has=page.get_by_label("Password")
    # ).highlight()

    # ACTIONS

    # button = page.get_by_role("button", name="Block button").nth(1)
    # button.click()
    #
    # button.dblclick(delay=500)
    #
    # # press button by clicking
    # button.click(button="right", delay=500)
    #
    # # hold button by click
    # button.click(modifiers=["Control"])
    #
    # button.click(modifiers=["Shift", "Control"])
    #
    # outline_button = page.locator("button.btn-outline-primary")
    #
    # outline_button.hover()



















    time.sleep(5)
    browser.close()
