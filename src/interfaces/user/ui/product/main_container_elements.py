"""
Main Container Elements

This file contains XPath locators for the main container elements.
"""

class MainContainerElements:
    """
    Class containing XPath locators for main container elements.
    """
    
    # Main container
    div_main_container = "//div[@class='main-container']"
    
    # Main content
    div_main = "//div[@class='main']"
    h1_hidden = "//div[@class='main']/h1[@class='hidden']"
    
    # Main content wrapper
    div_main_content = "//div[@class='main']/div[@class='main-content']"
    
    # Content container
    div_content = "//div[@class='content']"
    
    # Page title
    div_page_title = "//div[@class='page-title']"
    span_text = "//div[@class='page-title']/span[@class='text']" 