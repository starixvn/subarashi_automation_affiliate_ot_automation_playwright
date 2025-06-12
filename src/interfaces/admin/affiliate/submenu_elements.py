class SubmenuElements:

    # Main container
    div_submenu_container = "//div[@class='sub-menu-container']"
    div_icon_container = "//div[@class='sub-menu-container']/div[@class='d-inline-block'][1]"
    img_affiliate_icon = "//div[@class='sub-menu-container']//img[contains(@src, 'i_affiliateslist.png')]"
    div_nav_container = "//div[@class='sub-menu-container']/div[@class='d-inline-block'][2]"
    
    # Navigation menu
    ul_nav = "//div[@class='sub-menu-container']//ul[@class='nav']"
    
    # Menu items
    li_affiliate_info = "//div[@class='sub-menu-container']//ul[@class='nav']/li[@class='nav-item'][1]"
    lnk_affiliate_info = "//div[@class='sub-menu-container']//ul[@class='nav']/li[1]/a[contains(@href, '/Affiliate')]"
    
    li_payment_request = "//div[@class='sub-menu-container']//ul[@class='nav']/li[@class='nav-item'][2]"
    lnk_payment_request = "//div[@class='sub-menu-container']//ul[@class='nav']/li[2]/a[contains(@href, '/PaymentRequest')]"
    
    li_revenue_group = "//div[@class='sub-menu-container']//ul[@class='nav']/li[@class='nav-item'][3]"
    lnk_revenue_group = "//div[@class='sub-menu-container']//ul[@class='nav']/li[3]/a[contains(@href, '/RevenueGroup')]"
    
    li_email_history = "//div[@class='sub-menu-container']//ul[@class='nav']/li[@class='nav-item'][4]"
    lnk_email_history = "//div[@class='sub-menu-container']//ul[@class='nav']/li[4]/a[contains(@href, '/EmailHistory')]"
    
    # Active menu indicator
    lnk_active_menu = "//div[@class='sub-menu-container']//a[@class='nav-link active']"
    
    # Helper methods
    @staticmethod
    def lnk_menu_by_index(index):
        return f"//div[@class='sub-menu-container']//ul[@class='nav']/li[{index}]/a"
    
    @staticmethod
    def lnk_menu_by_text(menu_text):
        return f"//div[@class='sub-menu-container']//ul[@class='nav']//a[contains(text(), '{menu_text}')]" 