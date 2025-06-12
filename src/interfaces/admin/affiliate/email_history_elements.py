class EmailHistoryElements:
    # Loader elements
    div_loader = "//div[@class='loader']"
    div_backdrop = "//div[@class='backdrop']"
    div_spinner = "//div[@class='spinner']"
    
    # Filter section
    div_filter_container = "//div[@class='filter-container']"
    
    # Search By dropdown
    lbl_search_by = "//div[@class='filter-container']//label[text()='Search By']"
    sel_search_by = "//div[@class='filter-container']//select[@name='searchBy']"
    opt_all = "//div[@class='filter-container']//select[@name='searchBy']/option[@value='0']"
    opt_sender = "//div[@class='filter-container']//select[@name='searchBy']/option[@value='1']"
    opt_email = "//div[@class='filter-container']//select[@name='searchBy']/option[@value='2']"
    opt_affiliate = "//div[@class='filter-container']//select[@name='searchBy']/option[@value='3']"
    opt_unknown_affiliate = "//div[@class='filter-container']//select[@name='searchBy']/option[@value='4']"
    
    # Search Text field
    lbl_search_text = "//div[@class='filter-container']//label[text()='Search Text']"
    inp_search_text = "//div[@class='filter-container']//input[@name='searchText']"
    
    # All Date checkbox
    lbl_all_date = "//div[@class='filter-container']//label[@class='form-check-label']"
    chk_all_date = "//div[@class='filter-container']//input[@name='isGetAll']"
    
    # From date picker
    lbl_from = "//div[@class='filter-container']//label[text()='From']"
    div_from_daterange_container = "(//div[@class='filter-container']//div[@class='daterange-container'])[1]"
    div_from_daterange_label = "(//div[@class='filter-container']//div[@class='daterange-label'])[1]"
    inp_from_date = "(//div[@class='filter-container']//input[@class='input-text datepicker'])[1]"
    icon_from_calendar = "(//div[@class='filter-container']//span[@class='oi oi-calendar icon-calendar ml-1'])[1]"
    div_from_overlay = "(//div[@class='filter-container']//div[@class='overlay'])[1]"
    
    # Calendar elements - From date
    btn_from_prev_month = "(//button[@class='rdr-MonthAndYear-button prev'])[1]"
    sel_from_month = "(//span[@class='rdr-MonthAndYear-month']/select)[1]"
    sel_from_year = "(//span[@class='rdr-MonthAndYear-year']/select)[1]"
    btn_from_next_month = "(//button[@class='rdr-MonthAndYear-button next'])[1]"
    
    # To date picker
    lbl_to = "//div[@class='filter-container']//label[text()='To']"
    div_to_daterange_container = "(//div[@class='filter-container']//div[@class='daterange-container'])[2]"
    div_to_daterange_label = "(//div[@class='filter-container']//div[@class='daterange-label'])[2]"
    inp_to_date = "(//div[@class='filter-container']//input[@class='input-text datepicker'])[2]"
    icon_to_calendar = "(//div[@class='filter-container']//span[@class='oi oi-calendar icon-calendar ml-1'])[2]"
    div_to_overlay = "(//div[@class='filter-container']//div[@class='overlay'])[2]"
    
    # Calendar elements - To date
    btn_to_prev_month = "(//button[@class='rdr-MonthAndYear-button prev'])[2]"
    sel_to_month = "(//span[@class='rdr-MonthAndYear-month']/select)[2]"
    sel_to_year = "(//span[@class='rdr-MonthAndYear-year']/select)[2]"
    btn_to_next_month = "(//button[@class='rdr-MonthAndYear-button next'])[2]"
    
    # Search button
    btn_search = "//div[@class='filter-container']//button[@class='btn btn-outline-primary']"
    icon_search = "//div[@class='filter-container']//span[@class='oi oi-magnifying-glass']"
    
    # Main content area
    div_data_content = "//div[@class='data-content']"
    
    # Delete button
    btn_delete = "//div[@class='data-content']//button[@class='btn btn-outline-danger']"
    icon_delete = "//div[@class='data-content']//span[@class='oi oi-trash ml-2']"
    
    # Select All/None buttons
    spn_select = "//div[@class='data-content']//span[text()='Select:']"
    btn_select_all = "//div[@class='data-content']//button[@class='text-dark font-weight-bold btn btn-link'][1]"
    btn_select_none = "//div[@class='data-content']//button[@class='text-dark font-weight-bold btn btn-link'][2]"
    
    # Table container
    div_table_responsive = "//div[@class='table-responsive table-striped']"
    div_table_container = "//div[@class='table-container']"
    div_header_content = "//div[@class='header-content']"
    div_body_content = "//div[@class='body-content']"
    
    # Table headers
    tbl_header = "//div[@class='header-content']//table"
    th_checkbox = "//div[@class='header-content']//th[1]"
    th_number = "//div[@class='header-content']//th[@title='#']"
    th_sender = "//div[@class='header-content']//th[@title='Sender']"
    th_affiliate = "//div[@class='header-content']//th[@title='Affiliate']"
    th_subject = "//div[@class='header-content']//th[@title='Subject']"
    th_email_address = "//div[@class='header-content']//th[@title='Email Address']"
    th_sent_date = "//div[@class='header-content']//th[@title='Sent Date']"
    
    # Table body
    tbl_body = "//div[@class='body-content']//table"
    
    # First row cells (as examples)
    chk_email_row = "//div[@class='body-content']//tr[1]/td[1]/input[@type='checkbox']"
    td_row_number = "//div[@class='body-content']//tr[1]/td[@class='text-center' and @title='1']"
    td_sender = "//div[@class='body-content']//tr[1]/td[@title='đâsd']"
    td_affiliate = "//div[@class='body-content']//tr[1]/td[@title='dfgsgf']"
    td_subject = "//div[@class='body-content']//tr[1]/td[@title='wer']"
    btn_subject = "//div[@class='body-content']//tr[1]/td[@title='wer']/button"
    td_email = "//div[@class='body-content']//tr[1]/td[@title='wer@yopmail.com']"
    lnk_email = "//div[@class='body-content']//tr[1]/td[@title='wer@yopmail.com']/a"
    td_sent_date = "//div[@class='body-content']//tr[1]/td[@title='2025-04-28T00:00:30.83']"
    
    # Pagination section
    div_page_container = "//div[@class='page-container center-align']"
    lnk_page_first = "//a[@class='icon page-first disable']"
    lnk_page_prev = "//a[@class='icon page-prev disable']"
    div_page_input = "//div[@class='page-input']"
    inp_page = "//input[@class='page-form']"
    lnk_page_next = "//a[@class='icon page-next disable']"
    lnk_page_last = "//a[@class='icon page-last disable']"
    sel_page_size = "//select[@class='pagesize-select']"
    opt_page_size_10 = "//select[@class='pagesize-select']/option[@value='10']"
    opt_page_size_20 = "//select[@class='pagesize-select']/option[@value='20']"
    opt_page_size_50 = "//select[@class='pagesize-select']/option[@value='50']"
    opt_page_size_100 = "//select[@class='pagesize-select']/option[@value='100']"
    opt_page_size_200 = "//select[@class='pagesize-select']/option[@value='200']"
    opt_page_size_500 = "//select[@class='pagesize-select']/option[@value='500']"
    spn_page_info = "//span[@class='page-info']"
    
    # Helper methods for dynamic elements
    @staticmethod
    def chk_row_by_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[1]/input[@type='checkbox']"
    
    @staticmethod
    def td_number_by_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[2][@class='text-center']"
    
    @staticmethod
    def td_sender_by_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[3]"
    
    @staticmethod
    def td_affiliate_by_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[4]"
    
    @staticmethod
    def td_subject_by_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[5]"
    
    @staticmethod
    def btn_subject_by_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[5]/button"
    
    @staticmethod
    def td_email_by_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[6]"
    
    @staticmethod
    def lnk_email_by_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[6]/a"
    
    @staticmethod
    def td_sent_date_by_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[7][@class='text-center']" 