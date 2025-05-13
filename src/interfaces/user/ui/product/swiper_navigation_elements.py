"""
Swiper Navigation Elements

This file contains XPath locators for the swiper navigation elements.
"""

class SwiperNavigationElements:
    """
    Class containing XPath locators for swiper navigation elements.
    """
    
    @staticmethod
    def get_swiper_button_next(product_id):
        """
        Returns XPath for the next button in a product's swiper
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        slider_type = "auto-slider"
        if product_id in ["Lottery", "Esports", "Keno", "P2P", "NumberGame"]:
            slider_type = "manual-slider"
            
        return f"//div[@class='wrapper-items'][@id='{product_id}']//div[@class='swiper products-slider {slider_type}']//div[@class='swiper-button-next']"
    
    @staticmethod
    def get_swiper_button_prev(product_id):
        """
        Returns XPath for the previous button in a product's swiper
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        slider_type = "auto-slider"
        if product_id in ["Lottery", "Esports", "Keno", "P2P", "NumberGame"]:
            slider_type = "manual-slider"
            
        return f"//div[@class='wrapper-items'][@id='{product_id}']//div[@class='swiper products-slider {slider_type}']//div[@class='swiper-button-prev']"
    
    @staticmethod
    def get_swiper_pagination(product_id):
        """
        Returns XPath for the pagination element in a product's swiper
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        slider_type = "auto-slider"
        if product_id in ["Lottery", "Esports", "Keno", "P2P", "NumberGame"]:
            slider_type = "manual-slider"
            
        return f"//div[@class='wrapper-items'][@id='{product_id}']//div[@class='swiper products-slider {slider_type}']//div[@class='swiper-pagination']"
    
    @staticmethod
    def get_pagination_bullet(product_id, index=1):
        """
        Returns XPath for a specific pagination bullet in a product's swiper
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
            index: The 1-based index of the pagination bullet
        """
        slider_type = "auto-slider"
        if product_id in ["Lottery", "Esports", "Keno", "P2P", "NumberGame"]:
            slider_type = "manual-slider"
            
        return f"//div[@class='wrapper-items'][@id='{product_id}']//div[@class='swiper products-slider {slider_type}']//div[@class='swiper-pagination']/span[@class='swiper-pagination-bullet'][{index}]"
    
    @staticmethod
    def get_active_pagination_bullet(product_id):
        """
        Returns XPath for the active pagination bullet in a product's swiper
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        slider_type = "auto-slider"
        if product_id in ["Lottery", "Esports", "Keno", "P2P", "NumberGame"]:
            slider_type = "manual-slider"
            
        return f"//div[@class='wrapper-items'][@id='{product_id}']//div[@class='swiper products-slider {slider_type}']//div[@class='swiper-pagination']/span[@class='swiper-pagination-bullet swiper-pagination-bullet-active']"
    
    @staticmethod
    def get_next_button_svg(product_id):
        """
        Returns XPath for the SVG icon in the next button of a product's swiper
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        slider_type = "auto-slider"
        if product_id in ["Lottery", "Esports", "Keno", "P2P", "NumberGame"]:
            slider_type = "manual-slider"
            
        return f"//div[@class='wrapper-items'][@id='{product_id}']//div[@class='swiper products-slider {slider_type}']//div[@class='swiper-button-next']/svg"
    
    @staticmethod
    def get_prev_button_svg(product_id):
        """
        Returns XPath for the SVG icon in the previous button of a product's swiper
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        slider_type = "auto-slider"
        if product_id in ["Lottery", "Esports", "Keno", "P2P", "NumberGame"]:
            slider_type = "manual-slider"
            
        return f"//div[@class='wrapper-items'][@id='{product_id}']//div[@class='swiper products-slider {slider_type}']//div[@class='swiper-button-prev']/svg" 