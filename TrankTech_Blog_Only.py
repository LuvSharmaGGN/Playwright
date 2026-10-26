from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto("https://www.tranktechnologies.com/")

     
    Blog=page.locator('(//a[text()="Blog"])[1]').click()
    app_dev=page.locator('(//a[text()="App Development"])[1]')
    web_dev=page.locator('(//a[text()="Web Development"])[1]')
    soft_devlop=page.locator('(//a[text()="Software Development"])[1]')
    digi_mark=page.locator('(//a[text()="Digital Marketing"])[1]')
    email_mark=page.locator('(//a[text()="Email Marketing"])[1]')
    a_i=page.locator('(//a[text()="Artificial Intelligence"])[2]')
    ui_ux=page.locator('(//a[text()="UI UX Design"])[1]')
    
    blog_list=[app_dev,web_dev,soft_devlop,digi_mark,email_mark,a_i,ui_ux]

    for i in blog_list:
        i.click()
        page.wait_for_load_state('load')
        page.go_back()
    page.go_back()