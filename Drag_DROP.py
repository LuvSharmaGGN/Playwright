from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto("https://www.globalsqa.com/demo-site/draganddrop/#google_vignette")

    page.wait_for_load_state("load")

    f=page.frame_locator('(//iframe[@class="demo-frame"])[1]')

    image1=f.locator('//img[@alt="The peaks of High Tatras"]')

    image2=f.locator('//img[@alt="The chalet at the Green mountain lake"]')

    image3=f.locator('//img[@alt="Planning the ascent"]')

    image4=f.locator('//img[@alt="On top of Kozi kopka"]')

    trash =f.locator('//div[@id="trash"]')

    images=[image1,image2,image3,image4]

    for i in images:
        i.drag_to(trash)

    page.wait_for_timeout(2000)
    
    browser.close()

