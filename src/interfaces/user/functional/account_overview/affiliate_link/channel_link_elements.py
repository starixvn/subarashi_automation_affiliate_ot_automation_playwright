class ChannelLinkElements:

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
    