class SubmenuElements:
    
    # Submenu container
    div_submenu = "//div[@class='sub-menu-container pt-1']"
    ul_nav = "//div[@class='sub-menu-container pt-1']/ul[@class='nav']"
    
    # Navigation items
    li_referrers = "//div[@class='sub-menu-container pt-1']//li[@class='nav-item'][1]"
    lnk_referrers = "//div[@class='sub-menu-container pt-1']//li[@class='nav-item'][1]/a"
    lnk_referrers_active = "//div[@class='sub-menu-container pt-1']//li[@class='nav-item'][1]/a[@class='nav-link active']"
    
    li_landing_pages = "//div[@class='sub-menu-container pt-1']//li[@class='nav-item'][2]"
    lnk_landing_pages = "//div[@class='sub-menu-container pt-1']//li[@class='nav-item'][2]/a"
    lnk_landing_pages_active = "//div[@class='sub-menu-container pt-1']//li[@class='nav-item'][2]/a[@class='nav-link active']"
    
    li_marketing_page = "//div[@class='sub-menu-container pt-1']//li[@class='nav-item'][3]"
    lnk_marketing_page = "//div[@class='sub-menu-container pt-1']//li[@class='nav-item'][3]/a"
    lnk_marketing_page_active = "//div[@class='sub-menu-container pt-1']//li[@class='nav-item'][3]/a[@class='nav-link active']" 