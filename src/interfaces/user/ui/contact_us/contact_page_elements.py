"""
Contact Page Elements

This file contains XPath locators for the main elements on the Contact page.
"""

class ContactPageElements:
    """
    Class containing XPath locators for Contact page elements.
    """
    
    # Main container elements
    div_main_container = "//div[@class='main-container']"
    div_main = "//div[@class='main']/div[@class='main-content']"
    h1_hidden = "//div[@class='main']/h1[@class='hidden']"
    div_main_content = "//div[@class='main']/div[@class='main-content']"
    
    # Content elements
    div_content = "//div[@class='content']"
    div_page_title = "//div[@class='content']/div[@class='page-title']"
    span_text = "//div[@class='content']/div[@class='page-title']/span[@class='text']" 