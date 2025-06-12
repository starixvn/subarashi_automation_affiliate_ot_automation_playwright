class AccountOverviewElements:
    
    # Main container elements
    div_main_container = "//div[@class='main-container']"
    div_main_content = "//div[@class='main-content']"
    div_container_fluid = "//div[@class='container-fluid']"
    div_account_overview = "//div[@class='account-overview']"
    
    # Menu and tabs
    div_tab_menu = "//div[@class='tab-menu'][@id='account-overview-menu']"
    ul_menu = "//div[@id='account-overview-menu']/ul[@class='menu list-unstyled']"
    li_summary = "//div[@id='account-overview-menu']//li/a[@id='menuSummary']"
    li_affiliate_link = "//div[@id='account-overview-menu']//li/a[@id='menuAffiliateLink']"
    li_media_gallery = "//div[@id='account-overview-menu']//li/a[@id='menuMediaGallery']"
    
    # User info banner
    div_bg_orange = "//div[@class='account-overview']/div[@class='bg-orange']"
    span_last_login = "//div[@class='bg-orange']/span[@class='text'][1]"
    span_last_login_ip = "//div[@class='bg-orange']/span[@class='text'][2]"
    span_affiliate_id = "//div[@class='bg-orange']/span[@class='text'][3]"
    
    # Content container
    div_account_overview_content = "//div[@id='account-overview-content']"
    