"""
Pagination Elements

This file contains XPath locators for the pagination elements.
"""

class PaginationElements:
    """
    Class containing XPath locators for pagination elements.
    """
    
    # Pagination container
    div_player_detail_pager = "//div[@class='player-detail-pager'][@id='player-detail-pager']"
    
    # Pager container
    div_pager_container = "//div[@class='player-detail-pager']/div[@class='pager-container']"
    
    # Navigation buttons
    a_page_first = "//div[@class='player-detail-pager']//a[@class='icon glyphicon glyphicon-fast-backward page-first']"
    a_page_prev = "//div[@class='player-detail-pager']//a[@class='icon glyphicon glyphicon-triangle-left page-prev']"
    div_page_input = "//div[@class='player-detail-pager']//div[@class='page-input']"
    span_text_page_info = "//div[@class='player-detail-pager']//div[@class='page-input']/span[@class='text-pageInfo']"
    a_page_next = "//div[@class='player-detail-pager']//a[@class='icon glyphicon glyphicon-triangle-right page-next']"
    a_page_last = "//div[@class='player-detail-pager']//a[@class='icon glyphicon glyphicon-fast-forward page-last']"
    
    # Page size selector
    select_pagesize = "//div[@class='player-detail-pager']//select[@class='pagesize-select']"
    option_10 = "//div[@class='player-detail-pager']//select[@class='pagesize-select']/option[@value='10']"
    option_20 = "//div[@class='player-detail-pager']//select[@class='pagesize-select']/option[@value='20']"
    option_50 = "//div[@class='player-detail-pager']//select[@class='pagesize-select']/option[@value='50']"
    option_100 = "//div[@class='player-detail-pager']//select[@class='pagesize-select']/option[@value='100']"
    option_200 = "//div[@class='player-detail-pager']//select[@class='pagesize-select']/option[@value='200']"
    
    # Disabled button states
    a_page_first_disabled = "//div[@class='player-detail-pager']//a[@class='icon glyphicon glyphicon-fast-backward page-first disable']"
    a_page_prev_disabled = "//div[@class='player-detail-pager']//a[@class='icon glyphicon glyphicon-triangle-left page-prev disable']"
    a_page_next_disabled = "//div[@class='player-detail-pager']//a[@class='icon glyphicon glyphicon-triangle-right page-next disable']"
    a_page_last_disabled = "//div[@class='player-detail-pager']//a[@class='icon glyphicon glyphicon-fast-forward page-last disable']"
    
    @staticmethod
    def get_pagesize_option_by_value(value):
        """
        Get the XPath for a specific page size option by its value.
        
        Args:
            value (str): The value of the option ('10', '20', '50', '100', '200').
            
        Returns:
            str: XPath locator for the specified page size option.
        """
        return f"//div[@class='player-detail-pager']//select[@class='pagesize-select']/option[@value='{value}']"
    
    @staticmethod
    def get_selected_pagesize_option():
        """
        Get the XPath for the currently selected page size option.
        
        Returns:
            str: XPath locator for the selected page size option.
        """
        return "//div[@class='player-detail-pager']//select[@class='pagesize-select']/option[@selected]"
    
    @staticmethod
    def is_navigation_button_disabled(button_type):
        """
        Check if a specific navigation button is disabled.
        
        Args:
            button_type (str): The type of button ('first', 'prev', 'next', 'last').
            
        Returns:
            str: XPath locator for the disabled state of the specified button.
        """
        if button_type.lower() == 'first':
            return "//div[@class='player-detail-pager']//a[contains(@class, 'page-first disable')]"
        elif button_type.lower() == 'prev':
            return "//div[@class='player-detail-pager']//a[contains(@class, 'page-prev disable')]"
        elif button_type.lower() == 'next':
            return "//div[@class='player-detail-pager']//a[contains(@class, 'page-next disable')]"
        elif button_type.lower() == 'last':
            return "//div[@class='player-detail-pager']//a[contains(@class, 'page-last disable')]"
        else:
            return f"//div[@class='player-detail-pager']//a[contains(@class, 'page-{button_type.lower()} disable')]"