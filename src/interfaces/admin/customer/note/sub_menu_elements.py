class SubMenuElements:
    
    # Menu container
    ul_nav_menu = "//ul[@class='nav']"
    
    # Menu items by position
    li_menu_item_first = "//ul[@class='nav']/li[@class='nav-item'][1]"
    li_menu_item_second = "//ul[@class='nav']/li[@class='nav-item'][2]"
    
    # Menu links
    lnk_note = "//ul[@class='nav']/li[@class='nav-item'][1]/a[@class='nav-link']"
    lnk_marketing_team_note = "//ul[@class='nav']/li[@class='nav-item'][2]/a[@class='nav-link']"
    
    # Dynamic method to get menu item by index (1-based)
    @staticmethod
    def li_menu_item_by_index(index):
        return f"//ul[@class='nav']/li[@class='nav-item'][{index}]"
    
    # Dynamic method to get menu link by index (1-based)
    @staticmethod
    def lnk_menu_by_index(index):
        return f"//ul[@class='nav']/li[@class='nav-item'][{index}]/a[@class='nav-link']"
    
    # Active link detection
    lnk_active = "//ul[@class='nav']/li[@class='nav-item']/a[@class='nav-link active']" 