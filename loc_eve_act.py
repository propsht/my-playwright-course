# Locators, Events, Actions

import time

from playwright.sync_api import sync_playwright

# counting performe time waiting elements
from time import perf_counter

# def on_load(page):
# print("Page loaded:", page)


# def on_load(request):
#     print("Request loaded:", request)

#
# def on_filechooser(file_chooser):
#     print("File chooser selected:")
#     file_chooser.set_files("file.txt")

# def on_dialog(dialog):
#     print("Dialog opened:", dialog)
#     dialog.accept()
#
# def on_dialog(dialog):
#     print("Dialog opened:", dialog)
#     dialog.accept("Playwrite Cool")


def on_download(download):
    print("Download started")
    download.save_as("nature2.jpg")


with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=5000)
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
    # page.goto("https://bootswatch.com/default/")
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

    ## INPUT
    # input =  page.get_by_placeholder("Enter email")
    #
    # input.fill("test@test.com")
    # time.sleep(5)
    # input.clear()
    #
    # input.type("test@test.com", delay = 200)
    # time.sleep(5)
    # input.clear()
    #
    # valid_input = page.get_by_label("Valid input").nth(0)
    # valid_input.input_value()

    ## Radio, Checkboxes and Switches
    # radio_option2 = page.get_by_label("Option two can be something else and selecting it will deselect option one")
    # radio_option2.check()
    #
    # radio_option1 = page.get_by_label("Option one is this and that—be sure to include why it's great")
    # radio_option1.check()
    #
    # checkbox1 = page.get_by_label("Default checkbox")
    # checkbox2 = page.get_by_label("Checked checkbox")
    #
    # checkbox1.check()
    # checkbox2.uncheck()
    # #set state of our checkbox
    # checkbox2.is_checked()
    #
    # checkbox1.set_checked(False)
    # checkbox1.click()
    #
    # switch = page.get_by_label("Default switch checkbox input")
    # switch.check()
    # switch.click()

    # ## Select Option From Option Menu
    #
    # select = page.get_by_label("Example select")
    # select.select_option("4")
    # select.select_option("2")
    # select.select_option("5")
    #
    # multi_select = page.get_by_label("Example multiple select")
    # multi_select.select_option(["2", "4"])
    #
    # ## DROPDOWN
    # dropdown = page.locator("button#btnGroupDrop1")
    # dropdown.click()
    #
    # dropdown_link = page.locator("div.dropdown-menu:visible a:text('Dropdown link')").nth(1)
    # dropdown_link.click()

    ## Upload File

    # file_input = page.get_by_label("Default file input example")
    #
    # file_input.set_input_files("file.txt")
    # # file_input.set_input_files(["file.txt", "app.py"])
    #
    # #when we have one button and after modal window opened
    # with page.expect_file_chooser() as fc_info:
    #     file_input.click()
    #
    #     file_chooser = fc_info.value
    #     file_chooser.set_files("file2.txt")
    #
    #
    # #Keyboard Shorcuts
    # textarea = page.get_by_label("Example textarea")
    # textarea.fill("word")
    # textarea.clear()
    #
    # textarea.press("KeyW")
    # textarea.press("KeyO")
    # textarea.press("KeyR")
    # textarea.press("Shift+KeyD")
    # textarea.press("Control+ArrowLeft")
    # textarea.press("ArrowRight")
    #
    # button = page.get_by_role("button", name="Primary").nth(0)
    # button.click()
    #
    # link = page.locator("a.dropdown-item").nth(0)
    # link.click(force=True)
    #
    # print("Page loading...")
    # start = perf_counter()

    ## Waitings
    # page.goto(
    #     "https://playwright.dev/python/",
    #     # wait_until="load"
    #     # wait_until="domcontentloaded",
    #     # wait_until='commit',
    #     # wait_until='networkidle',
    # )
    #
    # time_taking = perf_counter() - start
    # print(f"Page loaded in {round(time_taking, 2)}s")

    ## Custom waitings
    # page.goto("https://www.scrapethissite.com/pages/ajax-javascript/")
    #
    # link = page.get_by_role("link", name="2015")
    # link.click()
    #
    # print("Loading oscars for 2015...")
    # start = perf_counter()
    #
    # # first_table_data = page.locator("td.film-title").nth(0)
    # # first_table_data.wait_for()
    # # first_table_data.wait_for(state="visible")
    # page.wait_for_selector(selector="td.film-title"),
    #
    # time_taking = perf_counter() - start
    # print(f"... movies are loaded, in  {round(time_taking, 2)}s")

    ##Event Listeners

    # page.on("load", on_load)
    # page.on("document", on_load)

    # page.on("request", on_load)
    # page.goto("https://bootswatch.com/default/")

    # page.on("filechooser", on_filechooser)
    # page.goto("https://bootswatch.com/default/")
    #
    # file_input = page.get_by_label("Default file input example")
    # file_input.click()

    ##Handling Dialigs

    # page.goto("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
    ## only OK btn
    # alert_btn = page.get_by_text("Show alert box")
    # alert_btn.click()

    ## Ok and Cancel btn
    # page.on("dialog", on_dialog)
    # alert_btn = page.get_by_text("Show confirm box")
    # alert_btn.click()

    # ## input some data in alert
    # page.on("dialog", on_dialog)
    # alert_btn = page.get_by_text("Show prompt box")
    # alert_btn.click()

    ## Download file
    # page.goto("https://unsplash.com/photos/brown-rock-formation-under-blue-sky-during-daytime-W2pwbgyn5RE")
    page.goto(
        "https://unsplash.com/photos/a-view-of-the-mountains-from-the-top-of-a-mountain-I62h3Pv-JSI"
    )

    # page.on("download", on_download)
    page.once("download", on_download)
    download_btn = page.get_by_role("link", name="Download free")

    with page.expect_download() as download_info:
        download_btn.click()

    # download = download_info.value
    # download.save_as("nature.jpg")
    print(f"Downloaded {download}")

    time.sleep(5)
    browser.close()
