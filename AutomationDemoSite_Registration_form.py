from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto("https://demo.automationtesting.in/Register.html")

    page.locator('//input[@placeholder="First Name"]').fill("Love")
    page.locator('//input[@placeholder="Last Name"]').fill("Sharma")

    page.locator('//textarea[@ng-model="Adress"]').fill("Gurgaon")

    page.locator('//input[@ng-model="EmailAdress"]').fill("love.ronit90@gmail.com")
    page.locator('//input[@ng-model="Phone"]').fill("8588854563")

    page.locator('//input[@value="Male"]').check()

    page.locator('//input[@value="Cricket"]').click()

    page.locator('//div[@class="ui-autocomplete-multiselect ui-state-default ui-widget"]').click()
    print("Clicking Hindi")
    l1=page.locator('//a[text()="English"]')
    l2=page.locator('//a[text()="Hindi"]')
    print("Clicking English")
    L = [l1, l2]
    for i in L:
        print("Entering loop")
        i.click()
    page.locator('//label[text()="Skills"]').click()

    page.locator('//select[@id="Skills"]').click()
    page.locator('//select[@id="Skills"]').select_option("Python")
    
    print("Selecting Country")
    page.locator('//span[@aria-labelledby="select2-country-container"]').click()
    print("Contry click successfull")
    page.wait_for_timeout(1000)
    page.locator("//input[@type='search']").fill('india')
    page.wait_for_timeout(1000)
    page.locator("//input[@type='search']").press("Enter")
   
    page.locator('//select[@id="yearbox"]').select_option("1990")
    page.locator('//select[@ng-model="monthbox"]').select_option("October")
    page.locator('//select[@id="daybox"]').select_option("28")
    page.locator('//input[@id="firstpassword"]').fill("Password12!")
    page.locator('//input[@id="secondpassword"]').fill("Password12!")
    
    

    page.locator('//button[@id="submitbtn"]').click()

    browser.close()





