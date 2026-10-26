from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://demoblaze.com/")
    page.locator('//a[@id="signin2"]').click()
    page.locator('//input[@id="sign-username"]').fill("love.ronit90@gmai.com")
    page.locator('//input[@id="sign-password"]').fill("Password12!")
    page.locator('//button[@onclick="register()"]').click()
    page.wait_for_timeout(5000)
    browser.close()