from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto("https://www.tranktechnologies.com/healthcare-mobile-app-development-company")

    Blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]').click()

    appDev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[2]')
    ai=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]')
    contentMKTng=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"]')
    crmDev=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
    digitalMKTNG=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
    ecomm=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
    email=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')
    graphicsDsgn=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
    sw_company=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
    swDev=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
    uiUx=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
    webDev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')
        
    blog_list=[appDev,ai,contentMKTng,crmDev,digitalMKTNG,ecomm,email,graphicsDsgn,sw_company,swDev,uiUx,webDev]
        
    for i in blog_list:
        i.click()
        page.wait_for_load_state('load')
        page.go_back()

    