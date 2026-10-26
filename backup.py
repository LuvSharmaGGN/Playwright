from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto("https://www.tranktechnologies.com/healthcare-mobile-app-development-company")

    #Vertical
    page.locator('//a[text()="Verticals"]').first.hover()

    #Trading and stock trading
    page.locator('//strong[text()="Trading"]').first.hover()
    page.locator('//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"]').first.click()
    page.go_back()

    #Trading and paper trading
    page.locator('//a[text()="Verticals"]').first.hover()
    page.locator('//strong[text()="Trading"]').first.hover()
    page.locator('//a[text()="Paper Trading"]').first.click()
    page.go_back()

    #Trading and CFD Training
    page.locator('//a[text()="Verticals"]').first.hover()
    page.locator('//strong[text()="Trading"]').first.hover()
    page.locator('//a[text()="CFD Trading"]').first.click()
    page.go_back()

    #Trading and TRading APP Development
    page.locator('//a[text()="Verticals"]').first.hover()
    page.locator('//strong[text()="Trading"]').first.hover()
    page.locator('//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"]').first.click()
    page.go_back()

    #Trading and Algo trading
    page.locator('//a[text()="Verticals"]').first.hover()
    page.locator('//strong[text()="Trading"]').first.hover()
    page.locator('//a[text()="Algo Trading"]').first.click()
    page.go_back()

    #Trading and Custom Trading
    page.locator('//a[text()="Verticals"]').first.hover()
    page.locator('//strong[text()="Trading"]').first.hover()
    page.locator('//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"]').first.click()
    page.go_back()

    #Trading and Web Portal Training
    page.locator('//a[text()="Verticals"]').first.hover()
    page.locator('//strong[text()="Trading"]').first.hover()
    page.locator('//a[text()="Web Portal Trading"]').first.click()
    page.go_back()