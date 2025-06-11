class SubmenuElements:
    # submenu_container
    div_submenu_container = "//div[@class='user-panel-menu-container']"

    # submenu_item
    statement_history = "//div[@class='user-panel-menu-container']/ul/li[1]/a"
    edit = "//div[@class='user-panel-menu-container']/ul/li[2]/a"
    note = "//div[@class='user-panel-menu-container']/ul/li[3]/a"
    player_detail = "//div[@class='user-panel-menu-container']/ul/li[4]/a"
    adjustments = "//div[@class='user-panel-menu-container']/ul/li[5]/a"
    player = "//div[@class='user-panel-menu-container']/ul/li[6]/a"
    view_log = "//div[@class='user-panel-menu-container']/ul/li[7]/a"
    click_statistics = "//div[@class='user-panel-menu-container']/ul/li[8]/a"

    @staticmethod
    def li_menu_item_by_index(index):
        return f"//ul[@class='nav']/li[@class='nav-item'][{index}]"
    
    @staticmethod
    def lnk_menu_by_index(index):
        return f"//ul[@class='nav']/li[@class='nav-item'][{index}]/a[@class='nav-link']"
    
    @staticmethod
    def lnk_menu_by_text(text):
        return f"//ul[@class='nav']/li[@class='nav-item']/a[@class='nav-link'][text()='{text}']" 