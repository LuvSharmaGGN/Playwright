from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()

    # Testing reporsitory
    
    page.goto("https://demo.automationtesting.in/Alerts.html")
    
    page.once("dialog", lambda dialog: dialog.accept())
    page.locator('//div[@id="OKTab"]').click()

    page.locator('//a[@href="#CancelTab"]').click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator('//div[@class="tab-pane col-md-6 col-md-offset-1 col-xs-4 col-xs-offset-1 active"]').click()

    page.locator('//a[@href="#Textbox"]').click()
    page.once("dialog", lambda dialog: dialog.accept("Love"))
    page.locator('//button[text()="click the button to demonstrate the prompt box "]').click()
    page.wait_for_timeout(5000)