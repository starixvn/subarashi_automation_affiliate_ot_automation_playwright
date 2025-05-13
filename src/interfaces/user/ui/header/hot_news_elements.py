"""
Hot News Elements

This file contains XPath locators for hot news elements.
"""

class HotNewsElements:
    """
    Class containing XPath locators for hot news elements.
    """
    
    # Hot news container
    div_hot_news = "//div[@class='hot-news']"
    div_hot_news_inner = "//div[@class='hot-news']/div[@class='hot-news-inner']"
    
    # Hot news title and controls
    div_hn_title = "//div[@class='hot-news']//div[@class='hn-title']"
    div_title_box = "//div[@class='hot-news']//div[@class='title-box']"
    span_hot_news_label = "//div[@class='hot-news']//div[@class='title-box']/span"
    div_news_control = "//div[@class='hot-news']//div[@class='news-control']"
    a_btn_prev = "//div[@class='hot-news']//div[@class='news-control']/a[@class='btn-prev']"
    a_btn_next = "//div[@class='hot-news']//div[@class='news-control']/a[@class='btn-next']"
    
    # News marquee
    div_hn_content = "//div[@class='hot-news']//div[@class='hn-content']"
    div_marquee_wrapper = "//div[@class='hot-news']//div[@class='marquee-wrapper']"
    div_marquee = "//div[@class='hot-news']//div[@class='marquee-wrapper']/div[@class='marquee']"
    div_running_text = "//div[@class='hot-news']//div[@class='marquee']/div[@class='running-text']"
    
    # News items
    span_news_dot = "//div[@class='hot-news']//div[@class='running-text']/span[@class='dot']"
    
    @staticmethod
    def get_news_item_by_index(index):
        """
        Returns XPath for a news item by its index
        
        Args:
            index: The 1-based index of the news item
        """
        return f"//div[@class='hot-news']//div[@class='running-text']/span[contains(@class, 'hn-item')][{index}]" 