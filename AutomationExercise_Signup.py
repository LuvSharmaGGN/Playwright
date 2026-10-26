from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://automationexercise.com/login")
    page.wait_for_timeout(2000)
    page.locator('//input[@data-qa="signup-name"]').fill("Love Sharma")
    page.locator('//input[@data-qa="signup-email"]').fill("love.ronit90@gmail.com")
    page.locator('//button[@data-qa="signup-button"]').click()
    page.wait_for_timeout(5000)
    browser.close()