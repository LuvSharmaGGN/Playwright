from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto("https://www.tranktechnologies.com/")

    #hover items for vertical tab
    vertical=page.locator('(//a[text()="Verticals"])[1]')
    trading=page.locator('(//img[@alt="trading"])[1]')
    retail_and_ecommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
    healthcare=page.locator('(//a[@href="https://www.tranktechnologies.com/healthcare-mobile-app-development-company"])[1]')
    fintech_mobile_app_development=page.locator('(//a[@href="https://www.tranktechnologies.com/fintech-mobile-app-development-company"])[1]')
    custom_App=page.locator('//strong[text()="Custom App"]')

    #Trading Sub Menu
    Stock_trading=page.locator('(//a[text()="Stock Trading"])[1]')
    algo_Trading=page.locator('(//a[text()="Algo Trading"])[1]')
    paper_trading=page.locator('(//a[text()="Paper Trading"])[1]')
    custom_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
    cfd_Trading=page.locator('(//a[text()="CFD Trading"])[1]')
    webportal_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
    stock_trading_development_massachusetts=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
    
    vertical_Trading=[Stock_trading,algo_Trading,paper_trading,custom_trading,cfd_Trading,webportal_trading,stock_trading_development_massachusetts]
        
    for i in vertical_Trading:
        vertical.hover()
        trading.hover()
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

    #Retail and Ecommerce
    ecommerce_web_development=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
    ecommerce_app_development=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
    
    retailAndEcommerce=[ecommerce_web_development,ecommerce_app_development]
    
    for i in retailAndEcommerce:
        vertical.hover()
        retail_and_ecommerce.hover()
        i.click()
        page.wait_for_load_state("load")
        page.go_back()
        
    #Healthcare
    diet_n_nutrition_app=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
    health_tracking_app=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
    
    healthcare_list=[diet_n_nutrition_app,health_tracking_app]
    
    for i in healthcare_list:
        vertical.hover()
        healthcare.hover()
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

    #Fintech
    pos_software=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
    crypto=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
    
    fintech_list=[pos_software,crypto]
    
    for i in fintech_list:
        vertical.hover()
        fintech_mobile_app_development.hover()
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

    #Custom APPS
    desktop_application_development=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
    crm_development_company=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
    hrm_application=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
    erp_app_development=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
    travel_mobile_app_development=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
    e_learning_mobile=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
    dating_app=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
    real_estate=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
    custom_crm_development=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
    
    custom_list=[desktop_application_development,crm_development_company,hrm_application,erp_app_development,travel_mobile_app_development,e_learning_mobile,
                     dating_app,real_estate,custom_crm_development]
    
    for i in custom_list:
        vertical.hover()
        custom_App.hover()
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

    #hover items for Technologies tab
    technologies=page.locator('(//a[text()="Technologies"])[1]')
    eCommerce_Development=page.locator('(//strong[text()="eCommerce Development"])[1]')
    Mobile_App_Development=page.locator('(//strong[text()="Mobile App Development"])[1]')
    Artificial_Intelligence=page.locator('(//strong[text()="Artificial Intelligence"])[1]')
    
    #eCommerce Development Tab under techonlogies
    Magento_Development=page.locator('//a[text()="Magento Development"]')
    opencart=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
    codeigniter=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
    wordpress=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
    big_commerce=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
    shopify=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
    cs_cart=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
    node_js=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
    nopcommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
    woocommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
    laravel=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
    prestashop=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
    drupal=page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
    wix=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
    joomla=page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
    react_js=page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
    express=page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')

    ecomm_list=[Magento_Development,opencart,codeigniter,wordpress,big_commerce,shopify,cs_cart,node_js,nopcommerce,woocommerce,laravel,prestashop,drupal,wix,
                    joomla,react_js,express]
    for i in ecomm_list:
        technologies.hover()
        eCommerce_Development.hover()
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

    # Mobile Development under technologies
    react=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
    enterprise_mobil_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
    xamarin=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
    kotlin=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
    flutter=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
    ionic=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
    swift=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
    appointment=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')   
    
    mobile=[react,enterprise_mobil_dev,xamarin,kotlin,flutter,ionic,swift,appointment]
    
    for i in mobile:
        technologies.hover()
        Mobile_App_Development.hover()
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

    # Artificial Intelligence under Tehcnologies
    technologies.hover()
    page.locator('(//strong[text()="Artificial Intelligence"])[1]').click(); 
    page.wait_for_timeout(5000)
    
    #blog categories
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
            
    blog_Category=[appDev,ai,contentMKTng,crmDev,digitalMKTNG,ecomm,email,graphicsDsgn,sw_company,swDev,uiUx,webDev]
            
    for i in blog_Category:
        i.click()
        page.wait_for_load_state('load')
        page.go_back()

    


