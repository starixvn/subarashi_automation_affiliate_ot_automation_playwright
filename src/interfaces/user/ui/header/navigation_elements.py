"""
Navigation Elements

This file contains XPath locators for navigation elements.
"""

class NavigationElements:
    """
    Class containing XPath locators for navigation elements.
    """
    
    # Navigation container
    div_nav_container = "//div[@class='nav-container']"
    div_navigation = "//div[@class='navigation']"
    div_menu_control = "//div[@class='menu-control']"
    
    # Menu button (mobile)
    div_btn_menu = "//div[@class='btn-menu'][@id='btnMenu']"
    div_hamburger_menu = "//div[@class='hamburger']"
    
    # Navigation menu
    nav_menu = "//nav[@class='main-menu']"
    ul_menu = "//nav[@class='main-menu']/ul"
    
    # Menu items
    li_home = "//nav[@class='main-menu']/ul/li[1]"
    a_home = "//nav[@class='main-menu']/ul/li[1]/a"
    li_sports = "//nav[@class='main-menu']/ul/li[2]"
    a_sports = "//nav[@class='main-menu']/ul/li[2]/a"
    li_esports = "//nav[@class='main-menu']/ul/li[3]"
    a_esports = "//nav[@class='main-menu']/ul/li[3]/a"
    li_live_casino = "//nav[@class='main-menu']/ul/li[4]"
    a_live_casino = "//nav[@class='main-menu']/ul/li[4]/a"
    li_slots = "//nav[@class='main-menu']/ul/li[5]"
    a_slots = "//nav[@class='main-menu']/ul/li[5]/a"
    li_lottery = "//nav[@class='main-menu']/ul/li[6]"
    a_lottery = "//nav[@class='main-menu']/ul/li[6]/a"
    li_fishing = "//nav[@class='main-menu']/ul/li[7]"
    a_fishing = "//nav[@class='main-menu']/ul/li[7]/a"
    li_promotions = "//nav[@class='main-menu']/ul/li[8]"
    a_promotions = "//nav[@class='main-menu']/ul/li[8]/a"
    li_vip = "//nav[@class='main-menu']/ul/li[9]"
    a_vip = "//nav[@class='main-menu']/ul/li[9]/a"
    
    # Support menu
    a_support = "//div[@class='nav-container']//a[@class='home-link']"
    a_live_chat = "//div[@class='nav-container']//a[@class='online-chat']"
    
    @staticmethod
    def get_menu_item_by_index(index):
        """
        Returns XPath for a menu item by its index
        
        Args:
            index: The 1-based index of the menu item
        """
        return f"//nav[@class='main-menu']/ul/li[{index}]"
    
    @staticmethod
    def get_menu_link_by_index(index):
        """
        Returns XPath for a menu link by its index
        
        Args:
            index: The 1-based index of the menu item
        """
        return f"//nav[@class='main-menu']/ul/li[{index}]/a"
    
    @staticmethod
    def get_menu_item_by_text(text):
        """
        Returns XPath for a menu item by its text
        
        Args:
            text: The text of the menu item
        """
        return f"//nav[@class='main-menu']/ul/li/a[contains(text(), '{text}')]/parent::li" 