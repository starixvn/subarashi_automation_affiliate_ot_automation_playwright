"""
Banner Elements

This file contains XPath locators for the top banner elements on the homepage.
"""

class BannerElements:
    """
    Class containing XPath locators for banner elements.
    """
    
    # Main content container
    div_main_content = "//div[@class='main-content']"
    
    # Content home page container
    div_content_home = "//div[@class='content home-page']"
    
    # Top banner container
    div_top_banner = "//div[@class='swiper top-banner']"
    div_swiper_wrapper = "//div[@class='swiper top-banner']/div[@class='swiper-wrapper']"
    div_swiper_slide = "//div[@class='swiper top-banner']/div[@class='swiper-wrapper']/div[@class='swiper-slide']"
    
    # Banner links
    a_desktop_banner = "//a[@class='nounderline home-banner-tracking show-pc']"
    a_mobile_banner = "//a[@class='nounderline home-banner-tracking show-mobile']"
    
    # Banner images
    img_desktop_banner = "//a[@class='nounderline home-banner-tracking show-pc']//img[@class='img-item img-responsive']"
    img_mobile_banner = "//a[@class='nounderline home-banner-tracking show-mobile']//img[@class='img-item img-responsive']"
    
    # Banner navigation
    div_swiper_pagination = "//div[@class='swiper top-banner']/div[@class='swiper-pagination']"
    
    @staticmethod
    def get_swiper_slide(index):
        """
        Returns XPath for a specific banner slide by index
        
        Args:
            index: The 1-based index of the slide
        """
        return f"//div[@class='swiper top-banner']/div[@class='swiper-wrapper']/div[@class='swiper-slide'][{index}]"
    
    @staticmethod
    def get_pagination_bullet(index):
        """
        Returns XPath for a specific pagination bullet by index
        
        Args:
            index: The 1-based index of the pagination bullet
        """
        return f"//div[@class='swiper top-banner']/div[@class='swiper-pagination']/span[@class='swiper-pagination-bullet'][{index}]" 