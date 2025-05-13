"""
Testimonial Elements

This file contains XPath locators for the affiliate testimonial section elements.
"""

class TestimonialElements:
    """
    Class containing XPath locators for the testimonial section elements.
    """
    
    # Section container
    div_block_aff_testimonial = "//div[@class='block block-aff-testimonial']"
    div_page_container = "//div[@class='block block-aff-testimonial']/div[@class='page-container']"
    
    # Section title
    h2_block_title = "//div[@class='block block-aff-testimonial']//h2[@class='block-title fill-color']"
    
    # Mini block container
    div_mini_block = "//div[@class='block block-aff-testimonial']//div[@class='mini-block']"
    
    # Testimonial slider
    div_swiper_testimonial = "//div[@class='swiper mini-block-testimonial']"
    div_swiper_wrapper = "//div[@class='swiper mini-block-testimonial']/div[@class='swiper-wrapper']"
    
    # Navigation buttons
    div_swiper_button_next = "//div[@class='swiper mini-block-testimonial']//div[@class='swiper-button-next']"
    div_swiper_button_prev = "//div[@class='swiper mini-block-testimonial']//div[@class='swiper-button-prev']"
    
    # Pagination
    div_swiper_pagination = "//div[@class='swiper mini-block-testimonial']//div[@class='swiper-pagination']"
    
    @staticmethod
    def get_testimonial_slide(index):
        """
        Returns XPath for a specific testimonial slide by index
        
        Args:
            index: The 1-based index of the testimonial slide
        """
        return f"//div[@class='swiper mini-block-testimonial']/div[@class='swiper-wrapper']/div[@class='swiper-slide'][{index}]"
    
    @staticmethod
    def get_testimonial_item(index):
        """
        Returns XPath for a specific testimonial item by index
        
        Args:
            index: The 1-based index of the testimonial slide
        """
        return f"//div[@class='swiper mini-block-testimonial']/div[@class='swiper-wrapper']/div[@class='swiper-slide'][{index}]/div[@class='items']"
    
    @staticmethod
    def get_affiliate_name(index):
        """
        Returns XPath for the affiliate name in a specific testimonial
        
        Args:
            index: The 1-based index of the testimonial slide
        """
        return f"//div[@class='swiper mini-block-testimonial']/div[@class='swiper-wrapper']/div[@class='swiper-slide'][{index}]/div[@class='items']/div[@class='aff-name']/span"
    
    @staticmethod
    def get_testimonial_title(index):
        """
        Returns XPath for the title in a specific testimonial
        
        Args:
            index: The 1-based index of the testimonial slide
        """
        return f"//div[@class='swiper mini-block-testimonial']/div[@class='swiper-wrapper']/div[@class='swiper-slide'][{index}]/div[@class='items']/div[@class='aff-testimonial']/div[@class='title']/span"
    
    @staticmethod
    def get_testimonial_content(index):
        """
        Returns XPath for the content in a specific testimonial
        
        Args:
            index: The 1-based index of the testimonial slide
        """
        return f"//div[@class='swiper mini-block-testimonial']/div[@class='swiper-wrapper']/div[@class='swiper-slide'][{index}]/div[@class='items']/div[@class='aff-testimonial']/div[@class='content']/span"
    
    @staticmethod
    def get_testimonial_rating(index):
        """
        Returns XPath for the rating in a specific testimonial
        
        Args:
            index: The 1-based index of the testimonial slide
        """
        return f"//div[@class='swiper mini-block-testimonial']/div[@class='swiper-wrapper']/div[@class='swiper-slide'][{index}]/div[@class='items']/div[@class='aff-vote']/img"
    
    @staticmethod
    def get_pagination_bullet(index):
        """
        Returns XPath for a specific pagination bullet
        
        Args:
            index: The 1-based index of the pagination bullet
        """
        return f"//div[@class='swiper mini-block-testimonial']//div[@class='swiper-pagination']/span[@class='swiper-pagination-bullet'][{index}]"