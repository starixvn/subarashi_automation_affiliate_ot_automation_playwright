class MarketingPageElements:
    
    # Filter section
    div_filter_container = "//div[@class='filter-container py-0']"
    div_form_inline = "//div[@class='filter-container py-0']/div[@class='form-inline']"
    
    # From date field
    div_from_date = "//div[@class='mr-sm-2 my-2 form-group'][1]"
    lbl_from_date = "//div[@class='mr-sm-2 my-2 form-group'][1]/label"
    div_from_daterange = "//div[@class='mr-sm-2 my-2 form-group'][1]//div[@class='daterange-container']"
    inp_from_date = "//div[@class='mr-sm-2 my-2 form-group'][1]//input[@class='input-text datepicker']"
    spn_from_calendar = "//div[@class='mr-sm-2 my-2 form-group'][1]//span[@class='oi oi-calendar']"
    
    # To date field
    div_to_date = "//div[@class='mr-sm-2 my-2 form-group'][2]"
    lbl_to_date = "//div[@class='mr-sm-2 my-2 form-group'][2]/label"
    div_to_daterange = "//div[@class='mr-sm-2 my-2 form-group'][2]//div[@class='daterange-container']"
    inp_to_date = "//div[@class='mr-sm-2 my-2 form-group'][2]//input[@class='input-text datepicker']"
    spn_to_calendar = "//div[@class='mr-sm-2 my-2 form-group'][2]//span[@class='oi oi-calendar']"
    
    # Language dropdown
    div_language = "//div[@class='mr-sm-2 my-2 form-group'][3]"
    lbl_language = "//label[@for='languageCode']"
    sel_language = "//select[@id='languageCode']"
    opt_all_languages = "//select[@id='languageCode']/option[@value='']"
    
    # Include Inactive checkbox
    div_include_inactive = "//div[@class='mr-sm-2 my-2 form-group'][4]"
    lbl_include_inactive = "//div[@class='mr-sm-2 my-2 form-group'][4]/label[@class='form-check-label']"
    chk_include_inactive = "//input[@name='includedInActive']"
    
    # Search button container
    div_search_button = "//div[@class='mr-sm-2 my-2 form-group'][5]"
    btn_search = "//button[contains(@class, 'btn-outline-primary')]"
    spn_search_icon = "//button[contains(@class, 'btn-outline-primary')]/span[@class='oi oi-magnifying-glass']"
    
    # Marketing Statistics container
    div_marketing_statistics = "//div[@class='data-content marketing-statistics']"
    
    # Table
    div_table_container = "//div[@class='data-content marketing-statistics']//div[@class='table-responsive table-striped my-2']"
    tbl_marketing = "//div[@class='data-content marketing-statistics']//div[@class='body-content']"
    
    # Table headers
    th_number = "//div[@class='data-content marketing-statistics']//th[@title='#']"
    th_channel = "//div[@class='data-content marketing-statistics']//th[@title='Channel']"
    th_language = "//div[@class='data-content marketing-statistics']//th[@title='Language']"
    th_total_click = "//div[@class='data-content marketing-statistics']//th[@title='Total Click']"
    th_unique_click = "//div[@class='data-content marketing-statistics']//th[@title='Unique Click']"
    th_signups = "//div[@class='data-content marketing-statistics']//th[@title='Signups']"
    th_fdm = "//div[@class='data-content marketing-statistics']//th[@title='FDM']"
    
    div_channel_wrapper = "//div[@class='p-0 th-wrapper']"
    spn_channel_text = "//div[@class='p-0 th-wrapper']/strong"
    div_icon_container = "//div[@class='p-0 th-wrapper']/div[@class='icon-container']"
    spn_caret_expand = "//div[@class='icon-container']/span[@class='caret expand current']"
    
    # Helper methods for pagination
    div_pagination = "//div[@class='page-container center-align']"
    a_page_first = "//div[@class='page-container center-align']/a[@class='icon page-first']"
    a_page_prev = "//div[@class='page-container center-align']/a[@class='icon page-prev']"
    div_page_input = "//div[@class='page-container center-align']/div[@class='page-input']"
    inp_page_number = "//div[@class='page-container center-align']//input[@class='page-form']"
    a_page_next = "//div[@class='page-container center-align']/a[@class='icon page-next']"
    a_page_last = "//div[@class='page-container center-align']/a[@class='icon page-last']"
    sel_page_size = "//div[@class='page-container center-align']/select[@class='pagesize-select']"
    spn_page_info = "//div[@class='page-container center-align']/span[@class='page-info']" 