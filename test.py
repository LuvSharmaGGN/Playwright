from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://www.tranktechnologies.com/healthcare-mobile-app-development-company"
    )

    print(1)

    Blog = page.locator('//a[@href="https://www.tranktechnologies.com/blog/"]')

    print(2)

    blog_list = [
        '//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"]',
        '//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]',
        '//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]'
    ]

    for i in blog_list:
        Blog.click()
        page.locator(i).click()
        print(4)
        page.wait_for_load_state("load")
        page.go_back()

    browser.close()