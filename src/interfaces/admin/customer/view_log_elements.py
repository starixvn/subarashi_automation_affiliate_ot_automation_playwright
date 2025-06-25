class ViewLogElements:
    
    # Filter section elements
    # Log type dropdown
    lbl_type = "//label[@for='logType']"
    sel_log_type = "//select[@id='logType']"
    opt_all = "//select[@id='logType']/option[@value='0']"
    opt_revenue_group = "//select[@id='logType']/option[@value='1']"
    opt_user_info = "//select[@id='logType']/option[@value='2']"
    opt_transaction = "//select[@id='logType']/option[@value='3']"
    opt_payout = "//select[@id='logType']/option[@value='4']"
    opt_permission = "//select[@id='logType']/option[@value='5']"
    opt_player = "//select[@id='logType']/option[@value='6']"
    
    # From date filter
    lbl_from = "//div[@class='mr-sm-2 form-group'][2]/label"
    div_from_date = "//div[@class='mr-sm-2 form-group'][2]//div[@class='daterange-container']"
    inp_from_date = "//div[@class='mr-sm-2 form-group'][2]//input[@class='input-text datepicker']"
    icn_from_calendar = "//div[@class='mr-sm-2 form-group'][2]//span[@class='oi oi-calendar']"
    
    # From date calendar elements
    sel_from_month = "//div[@class='mr-sm-2 form-group'][2]//span[@class='rdr-MonthAndYear-month']/select"
    sel_from_year = "//div[@class='mr-sm-2 form-group'][2]//span[@class='rdr-MonthAndYear-year']/select"
    btn_from_prev_month = "//div[@class='mr-sm-2 form-group'][2]//button[@class='rdr-MonthAndYear-button prev']"
    btn_from_next_month = "//div[@class='mr-sm-2 form-group'][2]//button[@class='rdr-MonthAndYear-button next']"
    
    # To date filter
    lbl_to = "//div[@class='mr-sm-2 form-group'][3]/label"
    div_to_date = "//div[@class='mr-sm-2 form-group'][3]//div[@class='daterange-container']"
    inp_to_date = "//div[@class='mr-sm-2 form-group'][3]//input[@class='input-text datepicker']"
    icn_to_calendar = "//div[@class='mr-sm-2 form-group'][3]//span[@class='oi oi-calendar']"
    
    # To date calendar elements
    sel_to_month = "//div[@class='mr-sm-2 form-group'][3]//span[@class='rdr-MonthAndYear-month']/select"
    sel_to_year = "//div[@class='mr-sm-2 form-group'][3]//span[@class='rdr-MonthAndYear-year']/select"
    btn_to_prev_month = "//div[@class='mr-sm-2 form-group'][3]//button[@class='rdr-MonthAndYear-button prev']"
    btn_to_next_month = "//div[@class='mr-sm-2 form-group'][3]//button[@class='rdr-MonthAndYear-button next']"
    
    # Search button
    btn_search = "//button[contains(@class, 'btn-outline-primary')]"
    
    # Table section
    div_data_content = "//div[@class='data-content']"
    tbl_logs = "//div[@class='table-responsive table-striped my-2']//table"
    
    # Table headers
    th_row_number = "//th[@title='#']"
    th_id = "//th[@title='ID']"
    th_date = "//th[@title='Date']"
    th_updated_by = "//th[@title='Updated By']"
    th_action = "//th[@title='Action']"
    th_description = "//th[@title='Description']"
    th_ip = "//th[@title='IP']"
    
    # Table body container
    div_table_body = "//div[@class='body-content']"
    
    # Pagination elements
    div_pagination = "//div[@class='page-container center-align']"
    btn_page_first = "//a[@class='icon page-first']"
    btn_page_prev = "//a[@class='icon page-prev']"
    inp_page_number = "//input[@class='page-form']"
    txt_total_pages = "//div[@class='page-input']/span[contains(text(), 'of')]"
    btn_page_next = "//a[@class='icon page-next']"
    btn_page_last = "//a[@class='icon page-last']"
    sel_page_size = "//select[@class='pagesize-select']"
    txt_page_info = "//span[@class='page-info']"
    
    # Helper methods for dynamic elements
    @staticmethod
    def get_log_type_option(value):
        """Returns XPath for a specific log type option by value"""
        return f"//select[@id='logType']/option[@value='{value}']"
    
    @staticmethod
    def get_log_type_option_by_text(text):
        """Returns XPath for a specific log type option by text"""
        return f"//select[@id='logType']/option[text()='{text}']"
    
    @staticmethod
    def get_day_in_calendar(day_number, is_from_calendar=True):
        """Returns XPath for a specific day button in the calendar"""
        calendar_section = "2" if is_from_calendar else "3"
        return f"//div[@class='mr-sm-2 form-group'][{calendar_section}]//span[@class='rdr-Day' and text()='{day_number}']"
    
    @staticmethod
    def get_row_by_id(log_id):
        """Returns XPath for a row with the specified log ID"""
        return f"//div[@class='body-content']//td[@title='{log_id}']/parent::tr"
    
    @staticmethod
    def get_row_by_updated_by(user_name):
        """Returns XPath for a row updated by the specified user"""
        return f"//div[@class='body-content']//td[@title='{user_name}' and contains(@class, 'text-center')]/parent::tr"
    
    @staticmethod
    def get_row_by_action(action_text):
        """Returns XPath for a row with the specified action"""
        return f"//div[@class='body-content']//td[@title='{action_text}' and contains(@class, 'text-center')]/parent::tr"
    
    @staticmethod
    def get_cell_by_row_and_column(row_number, column_index):
        """Returns XPath for a specific cell by row number and column index"""
        return f"//div[@class='body-content']//tbody/tr[{row_number}]/td[{column_index}]"
    
    @staticmethod
    def get_page_size_option(page_size):
        """Returns XPath for a specific page size option"""
        return f"//select[@class='pagesize-select']/option[@value='{page_size}']"
