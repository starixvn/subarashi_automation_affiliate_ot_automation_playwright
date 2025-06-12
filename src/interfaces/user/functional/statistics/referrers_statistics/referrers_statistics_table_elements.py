class ReferrersStatisticsTableElements:
    # Table container
    div_report_container = "//div[@class='report-container']"
    div_statistics_table = "//div[@id='statisticsTable']"
    
    # Table element
    table = "//div[@id='statisticsTable']/table"
    
    # Table header
    thead = "//div[@id='statisticsTable']/table/thead"
    tr_header = "//div[@id='statisticsTable']/table/thead/tr"
    
    # Header columns
    th_website_url = "//div[@id='statisticsTable']/table/thead/tr/th[1]"
    th_total_clicks = "//div[@id='statisticsTable']/table/thead/tr/th[2]"
    th_unique_clicks = "//div[@id='statisticsTable']/table/thead/tr/th[3]"
    th_signup = "//div[@id='statisticsTable']/table/thead/tr/th[4]"
    th_fdm = "//div[@id='statisticsTable']/table/thead/tr/th[5]"
    
    # Table body
    tbody = "//div[@id='statisticsTable']/table/tbody"
    tr_rows = "//div[@id='statisticsTable']/table/tbody/tr"
    
    # Row columns
    td_website_url = "//div[@id='statisticsTable']/table/tbody/tr/td[1]"
    td_total_clicks = "//div[@id='statisticsTable']/table/tbody/tr/td[2]"
    td_unique_clicks = "//div[@id='statisticsTable']/table/tbody/tr/td[3]"
    td_signup = "//div[@id='statisticsTable']/table/tbody/tr/td[4]"
    td_fdm = "//div[@id='statisticsTable']/table/tbody/tr/td[5]"
    
    # Website URL link
    a_statistics_item = "//div[@id='statisticsTable']/table/tbody/tr/td[1]/a[@class='statisticsItem']"