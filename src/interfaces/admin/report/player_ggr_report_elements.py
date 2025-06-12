class PlayerGgrReportElements:
    
    # Filter container elements
    inp_affiliate = "//input[@id='Affiliate']"
    lbl_affiliate = "//label[@for='Affiliate']"
    inp_player = "//input[@id='Player']"
    lbl_player = "//label[@for='Player']"
    sel_base_currency = "//select[@id='BaseCurrency']"
    lbl_base_currency = "//label[text()='Base Currency']"
    
    # Product selection elements
    div_product_selection = "//div[@class='multiple-select-container']"
    btn_product_selection = "//button[@class='multiple-select-default multiple-select-label']"
    txt_product_display = "//span[@class='text-display']"
    inp_product_search = "//input[@name='inputOption']"
    chk_product_all = "//input[@id='multiple-select-1-optionItemAll']"
    lbl_product_all = "//span[@for='multiple-select-1-optionItemAll']"
    
    # Date range elements
    lbl_date_from = "//label[text()='From']"
    inp_date_from = "//div[./label[text()='From']]/following-sibling::div//input[@class='input-text datepicker']"
    icn_calendar_from = "//div[./label[text()='From']]/following-sibling::div//span[@class='oi oi-calendar icon-calendar ml-1']"
    
    lbl_date_to = "//label[text()='To']"
    inp_date_to = "//div[./label[text()='To']]/following-sibling::div//input[@class='input-text datepicker']"
    icn_calendar_to = "//div[./label[text()='To']]/following-sibling::div//span[@class='oi oi-calendar icon-calendar ml-1']"
    
    # Calendar elements
    div_calendar = "//div[@class='rdr-Calendar']"
    sel_month = "//span[@class='rdr-MonthAndYear-month']/select"
    sel_year = "//span[@class='rdr-MonthAndYear-year']/select"
    btn_prev_month = "//button[@class='rdr-MonthAndYear-button prev']"
    btn_next_month = "//button[@class='rdr-MonthAndYear-button next']"
    
    # Search button
    btn_search = "//button[@class='btn btn-outline-primary']"
    icn_search = "//span[@class='oi oi-magnifying-glass']"
    
    # Report title and export elements
    div_report_title = "//div[@class='report-title']"
    btn_export_excel = "//button[@class='ml-auto btn btn-link btn-excel']"
    icn_export_excel = "//span[@class='oi icon-excel']"
    
    # Table elements
    tbl_report = "//table[@class='freeze-table table']"
    th_affiliate = "//th[@class='freeze-column-header freeze-column-header-0' and @title='Affiliate']"
    th_player = "//th[@class='freeze-column-header freeze-column-header-1' and @title='Player']"
    th_registration_date = "//th[@title='Registration Date']"
    th_fdm_date = "//th[@title='FDM Date']"
    
    # Table data rows
    tr_data_row = "//tbody/tr"
    td_affiliate = "//td[@class='freeze-column freeze-column-0']"
    td_player = "//td[@class='freeze-column freeze-column-1']"
    td_registration_date = "//tbody/tr/td[@class='text-center'][1]"
    td_fdm_date = "//tbody/tr/td[@class='text-center'][2]"
    
    # Turnover and GGR headers
    th_all_turnover = "//tr[@class='freeze-row freeze-row-h2']/th[@title='Turnover'][1]"
    th_all_ggr = "//tr[@class='freeze-row freeze-row-h2']/th[@title='GGR'][1]"
    
    # Turnover and GGR values in first data row
    td_all_turnover = "//tbody/tr/td[@class='text-right font-weight-bold'][1]"
    td_all_ggr = "//tbody/tr/td[@class='text-right font-weight-bold'][2]"
    
    # Footer totals
    td_total = "//tfoot/tr/td[@title='Total']"
    td_total_turnover = "//tfoot/tr/td[@class='text-right font-weight-bold'][1]"
    td_total_ggr = "//tfoot/tr/td[@class='text-right font-weight-bold'][2]"
    
    # Pagination elements
    div_pagination = "//div[@class='page-container center-align']"
    inp_page_number = "//input[@class='page-form']"
    btn_first_page = "//a[@class='icon page-first']"
    btn_prev_page = "//a[@class='icon page-prev']"
    btn_next_page = "//a[@class='icon page-next']"
    btn_last_page = "//a[@class='icon page-last']"
    sel_page_size = "//select[@class='pagesize-select']"
    spn_page_info = "//span[@class='page-info']" 