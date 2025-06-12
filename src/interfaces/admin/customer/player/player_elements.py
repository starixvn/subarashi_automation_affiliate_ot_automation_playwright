class PlayerElements:
    
    # Filter section elements
    # Player type dropdown
    lbl_player = "//label[@for='memberType']"
    sel_player_type = "//select[@id='memberType']"
    opt_player_select = "//select[@id='memberType']/option[@value='0']"
    opt_player_non_deposited = "//select[@id='memberType']/option[@value='1']"
    opt_player_deposited = "//select[@id='memberType']/option[@value='2']"
    
    # From date filter
    lbl_from = "//label[text()='From']"
    div_from_date = "//div[@class='my-2 mr-sm-2 form-group'][2]//div[@class='daterange-container']"
    inp_from_date = "//div[@class='my-2 mr-sm-2 form-group'][2]//input[@class='input-text datepicker']"
    icn_from_calendar = "//div[@class='my-2 mr-sm-2 form-group'][2]//span[@class='oi oi-calendar']"
    
    # From date calendar elements
    sel_from_month = "//div[@class='my-2 mr-sm-2 form-group'][2]//span[@class='rdr-MonthAndYear-month']/select"
    sel_from_year = "//div[@class='my-2 mr-sm-2 form-group'][2]//span[@class='rdr-MonthAndYear-year']/select"
    btn_from_prev_month = "//div[@class='my-2 mr-sm-2 form-group'][2]//button[@class='rdr-MonthAndYear-button prev']"
    btn_from_next_month = "//div[@class='my-2 mr-sm-2 form-group'][2]//button[@class='rdr-MonthAndYear-button next']"
    
    # To date filter
    lbl_to = "//label[text()='To']"
    div_to_date = "//div[@class='my-2 mr-sm-2 form-group'][3]//div[@class='daterange-container']"
    inp_to_date = "//div[@class='my-2 mr-sm-2 form-group'][3]//input[@class='input-text datepicker']"
    icn_to_calendar = "//div[@class='my-2 mr-sm-2 form-group'][3]//span[@class='oi oi-calendar']"
    
    # To date calendar elements
    sel_to_month = "//div[@class='my-2 mr-sm-2 form-group'][3]//span[@class='rdr-MonthAndYear-month']/select"
    sel_to_year = "//div[@class='my-2 mr-sm-2 form-group'][3]//span[@class='rdr-MonthAndYear-year']/select"
    btn_to_prev_month = "//div[@class='my-2 mr-sm-2 form-group'][3]//button[@class='rdr-MonthAndYear-button prev']"
    btn_to_next_month = "//div[@class='my-2 mr-sm-2 form-group'][3]//button[@class='rdr-MonthAndYear-button next']"
    
    # Get All checkbox
    lbl_get_all = "//label[contains(text(), 'Get All')]"
    chk_get_all = "//input[@name='isGetAll']"
    
    # Search button
    btn_search = "//button[contains(@class, 'btn-outline-primary')]"
    
    # Table section
    tbl_player = "//div[@class='table-responsive table-striped my-2']//table"
    
    # Table headers
    th_row_number = "//th[text()='#']"
    th_username = "//th[@title='User Name']"
    th_first_name = "//th[@title='First Name']"
    th_last_name = "//th[@title='Last Name']"
    th_email = "//th[@title='Email Address']"
    th_currency = "//th[@title='Currency']"
    th_registration_date = "//th[@title='Registration Date']"
    
    # Table body container
    div_table_body = "//div[@class='body-content']"
    
    # Pagination elements
    div_pagination = "//div[@class='page-container center-align']"
    btn_page_first = "//a[@class='icon page-first']"
    btn_page_prev = "//a[@class='icon page-prev']"
    inp_page_number = "//input[@class='page-form']"
    btn_page_next = "//a[@class='icon page-next']"
    btn_page_last = "//a[@class='icon page-last']"
    sel_page_size = "//select[@class='pagesize-select']"
    txt_page_info = "//span[@class='page-info']"
    
    # Helper methods for dynamic elements
    @staticmethod
    def get_day_in_calendar(day_number, is_from_calendar=True):
        """Returns XPath for a specific day button in the calendar"""
        calendar_section = "2" if is_from_calendar else "3"
        return f"//div[@class='my-2 mr-sm-2 form-group'][{calendar_section}]//span[@class='rdr-Day' and text()='{day_number}']"
    
    @staticmethod
    def get_row_by_username(username):
        """Returns XPath for a row with the specified username"""
        return f"//div[@class='body-content']//td[@title='{username}']/parent::tr"
    
    @staticmethod
    def get_cell_by_row_and_column(row_number, column_index):
        """Returns XPath for a specific cell by row number and column index"""
        return f"//div[@class='body-content']//tbody/tr[{row_number}]/td[{column_index}]"
    
    @staticmethod
    def get_page_size_option(page_size):
        """Returns XPath for a specific page size option"""
        return f"//select[@class='pagesize-select']/option[@value='{page_size}']"
