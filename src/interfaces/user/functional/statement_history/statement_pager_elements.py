class StatementPagerElements:

    # Pager container elements
    div_statement_pager = "//div[@id='statementPager']"
    div_pager_container = "//div[@id='statementPager']/div[@class='pager-container']"
    
    # Navigation buttons
    a_page_first = "//div[@id='statementPager']//a[@class='icon glyphicon glyphicon-fast-backward page-first']"
    a_page_prev = "//div[@id='statementPager']//a[@class='icon glyphicon glyphicon-triangle-left page-prev']"
    a_page_next = "//div[@id='statementPager']//a[@class='icon glyphicon glyphicon-triangle-right page-next']"
    a_page_last = "//div[@id='statementPager']//a[@class='icon glyphicon glyphicon-fast-forward page-last']"
    
    # Page info elements
    div_page_input = "//div[@id='statementPager']//div[@class='page-input']"
    span_text_page_info = "//div[@id='statementPager']//span[@class='text-pageInfo']"
    
    # Page size selector
    select_pagesize = "//div[@id='statementPager']//select[@class='pagesize-select']"
    option_pagesize_10 = "//div[@id='statementPager']//select[@class='pagesize-select']/option[@value='10']"
    option_pagesize_20 = "//div[@id='statementPager']//select[@class='pagesize-select']/option[@value='20']"
    option_pagesize_50 = "//div[@id='statementPager']//select[@class='pagesize-select']/option[@value='50']"
    option_pagesize_100 = "//div[@id='statementPager']//select[@class='pagesize-select']/option[@value='100']"
    option_pagesize_200 = "//div[@id='statementPager']//select[@class='pagesize-select']/option[@value='200']"
    
    # Data list container
    div_statement_data_list = "//div[@id='statementDataList']"
    
    # Total items hidden field
    input_total_item = "//input[@id='TotalItem']"