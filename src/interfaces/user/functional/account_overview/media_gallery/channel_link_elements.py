class ChannelLinkElements:
    """
    Class containing XPath locators for the Channel Link elements on the Affiliate page.
    These elements are used to manage channel links and their properties.
    """

    # Main container elements
    div_link_statistic = "//div[@id='linkStatistic']"
    div_channel_table = "//div[@id='linkStatistic']//div[@class='channel-table']"
    
    # Table elements
    table_channels = "//div[@id='linkStatistic']//table[@class='channels-table']"
    thead_channels = "//div[@id='linkStatistic']//table[@class='channels-table']/thead"
    tbody_channels = "//div[@id='linkStatistic']//table[@class='channels-table']/tbody"
    
    # Table header elements
    th_stt = "//div[@id='linkStatistic']//thead/tr/th[contains(@class, 'stt')]"
    th_channel = "//div[@id='linkStatistic']//thead/tr/th[contains(@class, 'channel')]"
    th_number_of_link = "//div[@id='linkStatistic']//thead/tr/th[contains(@class, 'number-of-link')]"
    th_lang = "//div[@id='linkStatistic']//thead/tr/th[contains(@class, 'lang')]"
    th_action = "//div[@id='linkStatistic']//thead/tr/th[contains(@class, 'action')]"
    
    # Table row elements
    tr_channel = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')]"
    
    # Channel details elements
    td_stt = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')]/td[contains(@class, 'stt')]"
    td_channel = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')]/td[contains(@class, 'channel')]"
    td_number_of_link = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')]/td[contains(@class, 'number-of-link')]"
    td_lang = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')]/td[contains(@class, 'lang')]"
    td_action = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')]/td[contains(@class, 'action')]"
    
    # Channel action buttons
    button_expand = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')]/td[contains(@class, 'action')]//button[contains(@class, 'btn-expand')]"
    
    # Child link elements
    tr_child_link = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'child-row')]"
    div_child_content = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'child-row')]/td/div[contains(@class, 'child-content')]"
    div_link_item = "//div[@id='linkStatistic']//div[contains(@class, 'link-item')]"
    
    # Link details elements
    div_link_main = "//div[@id='linkStatistic']//div[contains(@class, 'link-main')]"
    div_link_url = "//div[@id='linkStatistic']//div[contains(@class, 'link-url')]"
    input_link_url = "//div[@id='linkStatistic']//input[contains(@class, 'url-input')]"
    button_copy_url = "//div[@id='linkStatistic']//button[contains(@class, 'btn-copy-url')]"
    
    # Link info elements
    div_link_info = "//div[@id='linkStatistic']//div[contains(@class, 'link-info')]"
    span_link_id = "//div[@id='linkStatistic']//span[contains(@class, 'link-id')]"
    span_link_market = "//div[@id='linkStatistic']//span[contains(@class, 'link-market')]"
    span_link_clicks = "//div[@id='linkStatistic']//span[contains(@class, 'link-clicks')]"
    
    def get_channel_row_by_id(self, channel_id):
        """Get channel row by ID"""
        return f"//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row') and @data-id='{channel_id}']"
    
    def get_channel_row_by_index(self, index):
        """Get channel row by index (1-based)"""
        return f"//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')][{index}]"
    
    def get_channel_row_by_name(self, name):
        """Get channel row by channel name"""
        return f"//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')][.//td[contains(@class, 'channel') and contains(text(), '{name}')]]"
    
    def get_channel_expand_button(self, channel_id=None, channel_name=None, index=None):
        """Get expand button for a channel by ID, name, or index"""
        if channel_id:
            return f"//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row') and @data-id='{channel_id}']//button[contains(@class, 'btn-expand')]"
        elif channel_name:
            return f"//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')][.//td[contains(@class, 'channel') and contains(text(), '{channel_name}')]]//button[contains(@class, 'btn-expand')]"
        elif index:
            return f"//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')][{index}]//button[contains(@class, 'btn-expand')]"
        else:
            return self.button_expand
    
    def get_child_link_row(self, channel_id=None, channel_name=None, index=None):
        """Get child link row for a channel by ID, name, or index"""
        if channel_id:
            return f"//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row') and @data-id='{channel_id}']/following-sibling::tr[contains(@class, 'child-row')][1]"
        elif channel_name:
            return f"//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')][.//td[contains(@class, 'channel') and contains(text(), '{channel_name}')]]/following-sibling::tr[contains(@class, 'child-row')][1]"
        elif index:
            return f"//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')][{index}]/following-sibling::tr[contains(@class, 'child-row')][1]"
        else:
            return self.tr_child_link
    
    def get_child_links(self, channel_id=None, channel_name=None, index=None):
        """Get child link items for a channel by ID, name, or index"""
        if channel_id:
            return f"//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row') and @data-id='{channel_id}']/following-sibling::tr[contains(@class, 'child-row')][1]//div[contains(@class, 'link-item')]"
        elif channel_name:
            return f"//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')][.//td[contains(@class, 'channel') and contains(text(), '{channel_name}')]]/following-sibling::tr[contains(@class, 'child-row')][1]//div[contains(@class, 'link-item')]"
        elif index:
            return f"//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')][{index}]/following-sibling::tr[contains(@class, 'child-row')][1]//div[contains(@class, 'link-item')]"
        else:
            return self.div_link_item
    
    def get_link_url(self, channel_id=None, channel_name=None, index=None, link_index=1):
        """Get link URL input for a specific link item"""
        base_xpath = self.get_child_links(channel_id, channel_name, index)
        return f"({base_xpath})[{link_index}]//input[contains(@class, 'url-input')]"
    
    def get_copy_url_button(self, channel_id=None, channel_name=None, index=None, link_index=1):
        """Get copy URL button for a specific link item"""
        base_xpath = self.get_child_links(channel_id, channel_name, index)
        return f"({base_xpath})[{link_index}]//button[contains(@class, 'btn-copy-url')]"
    
    def get_link_id(self, channel_id=None, channel_name=None, index=None, link_index=1):
        """Get link ID span for a specific link item"""
        base_xpath = self.get_child_links(channel_id, channel_name, index)
        return f"({base_xpath})[{link_index}]//span[contains(@class, 'link-id')]"
    
    def get_link_market(self, channel_id=None, channel_name=None, index=None, link_index=1):
        """Get link market span for a specific link item"""
        base_xpath = self.get_child_links(channel_id, channel_name, index)
        return f"({base_xpath})[{link_index}]//span[contains(@class, 'link-market')]"
    
    def get_link_clicks(self, channel_id=None, channel_name=None, index=None, link_index=1):
        """Get link clicks span for a specific link item"""
        base_xpath = self.get_child_links(channel_id, channel_name, index)
        return f"({base_xpath})[{link_index}]//span[contains(@class, 'link-clicks')]" 