"""
Affiliate Page Elements

This file contains XPath locators for the main elements on the Affiliate page.
"""

class AffiliatePageElements:
    """
    Class containing XPath locators for Affiliate page elements.
    """
    
    # Main container elements
    div_main_container = "//div[@class='main-container']"
    div_main = "//div[@class='main']"
    h1_hidden = "//div[@class='main']/h1[@class='hidden']"
    div_main_content = "//div[@class='main-content']"
    
    # Content elements
    div_content = "//div[@class='content']"
    div_page_title = "//div[@class='page-title']"
    span_text = "//div[@class='page-title']/span[@class='text']"
    
    # Banner section
    div_top_banner = "//div[@class='swiper top-banner']"
    div_swiper_wrapper = "//div[@class='swiper top-banner']/div[@class='swiper-wrapper']"
    div_swiper_slide = "//div[@class='swiper top-banner']/div[@class='swiper-wrapper']/div[@class='swiper-slide']"
    a_banner_pc = "//div[@class='swiper-slide']/a[@class='nounderline promotion-banner-tracking show-pc']"
    a_banner_mobile = "//div[@class='swiper-slide']/a[@class='nounderline promotion-banner-tracking show-mobile']"
    img_banner_pc = "//div[@class='swiper-slide']/a[@class='nounderline promotion-banner-tracking show-pc']//img[@class='img-item img-responsive']"
    img_banner_mobile = "//div[@class='swiper-slide']/a[@class='nounderline promotion-banner-tracking show-mobile']//img[@class='img-item img-responsive']"
    div_swiper_pagination = "//div[@class='swiper top-banner']/div[@class='swiper-pagination']" 