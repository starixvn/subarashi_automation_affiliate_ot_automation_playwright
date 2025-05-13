"""
Product Elements

This file contains XPath locators for the products and providers section elements.
"""

class ProductElements:
    """
    Class containing XPath locators for the product section elements.
    """
    
    # Section container
    div_block_our_product = "//div[@class='block block-our-product']"
    div_page_container = "//div[@class='block block-our-product']/div[@class='page-container']"
    
    # Section title
    h2_block_title = "//div[@class='block block-our-product']//h2[@class='block-title fill-color']"
    span_show_pc = "//div[@class='block block-our-product']//h2[@class='block-title fill-color']/span[@class='show-pc']"
    
    # Content container
    div_block_content = "//div[@class='block block-our-product']/div[@class='page-container']/div[@class='block-content']"
    
    # Product wrapper
    div_wrapper_block = "//div[@class='block-our-product']//div[@class='wrapper-block']"
    div_items = "//div[@class='block-our-product']//div[@class='wrapper-block']/div[@class='items']"
    
    # Arrow elements
    span_arrow_1 = "//div[@class='block-our-product']//span[@class='arrow-products arrow-1']"
    span_arrow_2 = "//div[@class='block-our-product']//span[@class='arrow-products arrow-2']"
    span_arrow_3 = "//div[@class='block-our-product']//span[@class='arrow-products arrow-3']"
    span_arrow_4 = "//div[@class='block-our-product']//span[@class='arrow-products arrow-4']"
    
    # Provider banner
    div_mini_block = "//div[@class='block block-our-product']//div[@class='mini-block']"
    div_swiper_banner = "//div[@class='swiper mini-block-banner']"
    div_swiper_wrapper = "//div[@class='swiper mini-block-banner']/div[@class='swiper-wrapper']"
    
    # Provider navigation
    div_swiper_button_next = "//div[@class='swiper mini-block-banner']//div[@class='swiper-button-next']"
    div_swiper_button_prev = "//div[@class='swiper mini-block-banner']//div[@class='swiper-button-prev']"
    div_swiper_pagination = "//div[@class='swiper mini-block-banner']//div[@class='swiper-pagination']"
    
    @staticmethod
    def get_product_item(index):
        """
        Returns XPath for a specific product item by index
        
        Args:
            index: The 1-based index of the product item
        """
        return f"//div[@class='block-our-product']//div[@class='wrapper-block']/div[@class='items'][{index}]"
    
    @staticmethod
    def get_product_link(index):
        """
        Returns XPath for a specific product link by index
        
        Args:
            index: The 1-based index of the product item
        """
        return f"//div[@class='block-our-product']//div[@class='wrapper-block']/div[@class='items'][{index}]/a"
    
    @staticmethod
    def get_product_image(index):
        """
        Returns XPath for a specific product image by index
        
        Args:
            index: The 1-based index of the product item
        """
        return f"//div[@class='block-our-product']//div[@class='wrapper-block']/div[@class='items'][{index}]/a/img"
    
    @staticmethod
    def get_product_name(index):
        """
        Returns XPath for a specific product name by index
        
        Args:
            index: The 1-based index of the product item
        """
        return f"//div[@class='block-our-product']//div[@class='wrapper-block']/div[@class='items'][{index}]/a/span[@class='name-item']"
    
    @staticmethod
    def get_provider_slide(index):
        """
        Returns XPath for a specific provider slide by index
        
        Args:
            index: The 1-based index of the provider slide
        """
        return f"//div[@class='swiper mini-block-banner']/div[@class='swiper-wrapper']/div[@class='swiper-slide'][{index}]"
    
    @staticmethod
    def get_provider_image(index):
        """
        Returns XPath for a specific provider image by index
        
        Args:
            index: The 1-based index of the provider slide
        """
        return f"//div[@class='swiper mini-block-banner']/div[@class='swiper-wrapper']/div[@class='swiper-slide'][{index}]/img"
    
    @staticmethod
    def get_pagination_bullet(index):
        """
        Returns XPath for a specific pagination bullet
        
        Args:
            index: The 1-based index of the pagination bullet
        """
        return f"//div[@class='swiper mini-block-banner']//div[@class='swiper-pagination']/span[@class='swiper-pagination-bullet'][{index}]" 