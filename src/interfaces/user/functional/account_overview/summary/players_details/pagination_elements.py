class PaginationElements:
    
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