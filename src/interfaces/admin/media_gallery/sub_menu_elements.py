class SubMenuElements:
    # Main container
    div_sub_menu_container = "//div[@class='sub-menu-container']"
    
    # Image element
    img_media_icon = "//div[@class='d-inline-block']/img[contains(@src, 'i_media1.png')]"
    
    # Navigation links
    lnk_banner_list = "//ul[@class='nav']/li/a[text()='Banner List']"
    lnk_landing_page_list = "//ul[@class='nav']/li/a[text()='Landing Page List']"
    
    # Active navigation item (dynamically identifies the current active menu)
    lnk_active_menu = "//ul[@class='nav']/li/a[@class='nav-link active']" 