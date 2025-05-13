"""
Partnership Elements

This file contains XPath locators for the partnership and sponsorship section elements.
"""

class PartnershipElements:
    """
    Class containing XPath locators for the partnership section elements.
    """
    
    # Section container
    div_block_partnership = "//div[@class='block block-partnership']"
    div_page_container = "//div[@class='block block-partnership']/div[@class='page-container']"
    
    # Section title
    h2_block_title = "//div[@class='block block-partnership']//h2[@class='block-title fill-color']"
    span_block_mb = "//div[@class='block block-partnership']//h2[@class='block-title fill-color']/span[@class='block-mb']"
    
    # Content container
    div_block_content = "//div[@class='block block-partnership']/div[@class='page-container']/div[@class='block-content']"
    
    # Partnership banner slider
    div_swiper_partnership = "//div[@class='swiper partnership-banner']"
    div_swiper_wrapper = "//div[@class='swiper partnership-banner']/div[@class='swiper-wrapper']"
    
    # Navigation buttons
    div_swiper_button_next = "//div[@class='swiper partnership-banner']//div[@class='swiper-button-next']"
    div_swiper_button_prev = "//div[@class='swiper partnership-banner']//div[@class='swiper-button-prev']"
    
    # Pagination
    div_swiper_pagination = "//div[@class='swiper partnership-banner']//div[@class='swiper-pagination']"
    
    @staticmethod
    def get_partnership_slide(index):
        """
        Returns XPath for a specific partnership slide by index
        
        Args:
            index: The 1-based index of the partnership slide
        """
        return f"//div[@class='swiper partnership-banner']/div[@class='swiper-wrapper']/div[@class='swiper-slide'][{index}]"
    
    @staticmethod
    def get_partnership_image(index):
        """
        Returns XPath for a specific partnership image by index
        
        Args:
            index: The 1-based index of the partnership slide
        """
        return f"//div[@class='swiper partnership-banner']/div[@class='swiper-wrapper']/div[@class='swiper-slide'][{index}]/img"
    
    @staticmethod
    def get_arrow(index, position):
        """
        Returns XPath for an arrow in a specific partnership slide
        
        Args:
            index: The 1-based index of the partnership slide
            position: The position of the arrow (1, 2, 3, or 4)
        """
        return f"//div[@class='swiper partnership-banner']/div[@class='swiper-wrapper']/div[@class='swiper-slide'][{index}]/span[@class='partnership-products arrow-{position}']"
    
    @staticmethod
    def get_pagination_bullet(index):
        """
        Returns XPath for a specific pagination bullet
        
        Args:
            index: The 1-based index of the pagination bullet
        """
        return f"//div[@class='swiper partnership-banner']//div[@class='swiper-pagination']/span[@class='swiper-pagination-bullet'][{index}]" 