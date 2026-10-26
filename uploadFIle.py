from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto("https://demo.automationtesting.in/Register.html")
    page.set_input_files('//input[@onchange="uploadimg()"]',"D://Playwright//Screenshots//screenshot2.png")
    page.wait_for_timeout(5000)
    browser.close()