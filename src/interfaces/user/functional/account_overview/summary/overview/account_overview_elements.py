"""
Account Overview Elements

This file contains XPath locators for the main elements on the Account Overview page.
"""

class AccountOverviewElements:
    """
    Class containing XPath locators for Account Overview page elements.
    """
    
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
    
    @staticmethod
    def get_menu_item_by_id(menu_id):
        """
        Get the XPath for a specific menu item by its ID.
        
        Args:
            menu_id (str): The ID of the menu item (menuSummary, menuAffiliateLink, menuMediaGallery).
            
        Returns:
            str: XPath locator for the specified menu item.
        """
        return f"//div[@id='account-overview-menu']//li/a[@id='{menu_id}']"
    
    @staticmethod
    def get_menu_item_by_name(name):
        """
        Get the XPath for a specific menu item by its data-name attribute.
        
        Args:
            name (str): The data-name attribute value (Summary, AffiliateLink, MediaGallery).
            
        Returns:
            str: XPath locator for the specified menu item.
        """
        return f"//div[@id='account-overview-menu']//li/a[@data-name='{name}']"
    
    @staticmethod
    def get_active_menu_item():
        """
        Get the XPath for the currently active menu item.
        
        Returns:
            str: XPath locator for the active menu item.
        """
        return "//div[@id='account-overview-menu']//li/a[@class='menu-item account-overview-menu-item active']" 