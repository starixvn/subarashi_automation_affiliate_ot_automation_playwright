class ChannelLinkElements:
    """
    This class contains XPath locators for channel link elements on the affiliate page.
    """
    
    # Main container elements
    div_link_statistic = "//div[@id='link-statistic']"
    div_channel_table = "//div[@id='channel-table']"
    
    # Table elements
    table_channels = "//div[@id='channel-table']/table"
    thead_channels = "//div[@id='channel-table']/table/thead"
    tbody_channels = "//div[@id='channel-table']/table/tbody"
    
    # Table header elements
    th_stt = "//div[@id='channel-table']/table/thead/tr/th[@class='stt']"
    th_channel = "//div[@id='channel-table']/table/thead/tr/th[@class='channel']"
    th_number_of_link = "//div[@id='channel-table']/table/thead/tr/th[@class='number-of-link text-right']"
    th_lang = "//div[@id='channel-table']/table/thead/tr/th[@class='lang']"
    
    # Channel item elements (parent rows)
    tr_parent_item = "//div[@id='channel-table']/table/tbody/tr[@class='parent-item']"
    
    # Child row elements (hidden links)
    tr_parent_tr = "//div[@id='channel-table']/table/tbody/tr[@class='display-none parent-tr']"
    
    def get_channel_row_by_id(self, channel_id):
        """Get a channel row by its data-id attribute."""
        return f"//div[@id='channel-table']/table/tbody/tr[@data-id='{channel_id}']"
    
    def get_channel_row_by_index(self, index):
        """Get a channel row by its index (1-based)."""
        return f"//div[@id='channel-table']/table/tbody/tr[@class='parent-item'][{index}]"
    
    def get_channel_row_by_name(self, channel_name):
        """Get a channel row by its display name."""
        return f"//div[@id='channel-table']/table/tbody/tr[.//span[@class='flex-0'][text()='{channel_name}']]"
    
    def get_channel_name(self, channel_id):
        """Get the channel name element for a specific channel."""
        return f"//div[@id='channel-table']/table/tbody/tr[@data-id='{channel_id}']//span[@class='flex-0']"
    
    def get_channel_number_of_links(self, channel_id):
        """Get the number of links element for a specific channel."""
        return f"//div[@id='channel-table']/table/tbody/tr[@data-id='{channel_id}']/td[@class='text-center text-bold']"
    
    def get_dropdown_button(self, channel_id):
        """Get the dropdown button element for a specific channel."""
        return f"//div[@id='channel-table']/table/tbody/tr[@data-id='{channel_id}']//button[@class='btn btn-transparent btn-dropdown-table']"
    
    def get_chevron_icon(self, channel_id):
        """Get the chevron icon element for a specific channel."""
        return f"//div[@id='channel-table']/table/tbody/tr[@data-id='{channel_id}']//span[@class='chevron right']"
    
    # Child links for a specific channel
    def get_child_links(self, channel_id):
        """Get all child link rows for a specific channel."""
        return f"//div[@id='channel-table']/table/tbody/tr[@data-parent='{channel_id}']"
    
    def get_link_url(self, channel_id, index=1):
        """Get a specific link URL element for a channel by index."""
        return f"//div[@id='channel-table']/table/tbody/tr[@data-parent='{channel_id}'][{index}]/td[2]/a"
    
    def get_link_market(self, channel_id, index=1):
        """Get a specific link market element for a channel by index."""
        return f"//div[@id='channel-table']/table/tbody/tr[@data-parent='{channel_id}'][{index}]/td[@class='market-name']"
    
    def get_link_by_market(self, channel_id, market_name):
        """Get a link for a specific channel and market name."""
        return f"//div[@id='channel-table']/table/tbody/tr[@data-parent='{channel_id}']/td[@class='market-name'][text()='{market_name}']/preceding-sibling::td[1]/a" 