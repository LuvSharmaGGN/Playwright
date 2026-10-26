from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://demoblaze.com/")
    page.wait_for_timeout(5000)
    page.locator('//a[@id="login2"]').click()
    page.locator('//input[@id="loginusername"]').fill("love.ronit90@gmai.com")
    page.locator('//input[@id="loginpassword"]').fill("Password12!")
    page.locator('//button[text()="Log in"]').click()
    page.wait_for_timeout(5000)
    browser.close()