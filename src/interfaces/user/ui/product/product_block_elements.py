"""
Product Block Elements

This file contains XPath locators for the product block elements.
"""

class ProductBlockElements:
    """
    Class containing XPath locators for product block elements.
    """
    
    # Product block container
    div_block_items_products = "//div[@class='block block-items-products']"
    
    # Main items container
    div_main_items = "//div[@class='block block-items-products']/div[@class='main-items']"
    
    # Product wrapper items container
    div_wrapper_items = "//div[@class='main-items']/div[@class='wrapper-items']"
    div_wrapper_sports = "//div[@class='main-items']/div[@class='wrapper-items'][@id='Sports']"
    div_wrapper_live_casino = "//div[@class='main-items']/div[@class='wrapper-items'][@id='LiveCasino']"
    div_wrapper_slot = "//div[@class='main-items']/div[@class='wrapper-items'][@id='Slot']"
    div_wrapper_lottery = "//div[@class='main-items']/div[@class='wrapper-items'][@id='Lottery']"
    div_wrapper_esports = "//div[@class='main-items']/div[@class='wrapper-items'][@id='Esports']"
    div_wrapper_keno = "//div[@class='main-items']/div[@class='wrapper-items'][@id='Keno']"
    div_wrapper_p2p = "//div[@class='main-items']/div[@class='wrapper-items'][@id='P2P']"
    div_wrapper_number_game = "//div[@class='main-items']/div[@class='wrapper-items'][@id='NumberGame']"
    
    # Page container
    div_page_container = "//div[@class='wrapper-items']/div[@class='page-container']"
    
    # Items container (for individual product)
    div_items = "//div[@class='page-container']/div[@class='items']"
    
    @staticmethod
    def get_wrapper_by_id(product_id):
        """
        Returns XPath for a specific product wrapper by its ID
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        return f"//div[@class='main-items']/div[@class='wrapper-items'][@id='{product_id}']"
    
    @staticmethod
    def get_page_container_by_product_id(product_id):
        """
        Returns XPath for a page container within a specific product wrapper
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        return f"//div[@class='main-items']/div[@class='wrapper-items'][@id='{product_id}']/div[@class='page-container']"
    
    @staticmethod
    def get_items_by_product_id(product_id):
        """
        Returns XPath for items container within a specific product wrapper
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        return f"//div[@class='main-items']/div[@class='wrapper-items'][@id='{product_id}']/div[@class='page-container']/div[@class='items']" 