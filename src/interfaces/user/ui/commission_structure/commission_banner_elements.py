"""
Commission Banner Elements

This file contains XPath locators for the commission banner elements.
"""

class CommissionBannerElements:
    """
    Class containing XPath locators for commission banner elements.
    """
    
    # Banner container
    div_swiper_top_banner = "//div[@class='swiper top-banner']"
    div_swiper_wrapper = "//div[@class='swiper top-banner']/div[@class='swiper-wrapper']"
    div_swiper_slide = "//div[@class='swiper top-banner']/div[@class='swiper-wrapper']/div[@class='swiper-slide']"
    
    # Desktop banner
    a_desktop_banner = "//a[@class='nounderline commission-structure-banner-tracking show-pc']"
    picture_desktop = "//a[@class='nounderline commission-structure-banner-tracking show-pc']/picture"
    source_desktop_webp = "//a[@class='nounderline commission-structure-banner-tracking show-pc']/picture/source[@type='image/webp']"
    source_desktop_jpg = "//a[@class='nounderline commission-structure-banner-tracking show-pc']/picture/source[@type='image/jpeg']"
    img_desktop = "//a[@class='nounderline commission-structure-banner-tracking show-pc']/picture/img[@class='img-item img-responsive']"
    
    # Mobile banner
    a_mobile_banner = "//a[@class='nounderline commission-structure-banner-tracking show-mobile']"
    picture_mobile = "//a[@class='nounderline commission-structure-banner-tracking show-mobile']/picture"
    source_mobile_webp = "//a[@class='nounderline commission-structure-banner-tracking show-mobile']/picture/source[@type='image/webp']"
    source_mobile_jpg = "//a[@class='nounderline commission-structure-banner-tracking show-mobile']/picture/source[@type='image/jpeg']"
    img_mobile = "//a[@class='nounderline commission-structure-banner-tracking show-mobile']/picture/img[@class='img-item img-responsive']"
    
    # Pagination
    div_swiper_pagination = "//div[@class='swiper top-banner']/div[@class='swiper-pagination']" 