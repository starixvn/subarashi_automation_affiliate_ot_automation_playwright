class StatementHistoryElements:
    """
    Element selectors for the Customer Statement History page in the admin interface.
    
    Follows these criteria:
    - Each XPath selector targets a unique element
    - Uses IDs and unique classes where available
    - Avoids selectors that rely on text content
    - Follows a clear DOM structure
    """
    # Filter section
    div_filter_container = "//div[@class='filter-container']"
    div_form_inline = "//div[@class='filter-container']/div[@class='form-inline']"
    
    # From date filter
    div_from_group = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][1]"
    lbl_from = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][1]/label"
    div_from_daterange = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][1]/div[@class='daterange-container']"
    inp_from_date = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][1]//input[@class='input-text datepicker']"
    spn_from_calendar = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][1]//span[@class='oi oi-calendar icon-calendar ml-1']"
    
    # From date calendar overlay
    div_from_overlay = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][1]//div[@class='overlay']"
    div_from_calendar = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][1]//div[@class='rdr-Calendar']"
    btn_from_prev_month = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][1]//button[@class='rdr-MonthAndYear-button prev']"
    sel_from_month = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][1]//select[@class='rdr-MonthAndYearSelect'][1]"
    sel_from_year = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][1]//select[@class='rdr-MonthAndYearSelect'][2]"
    btn_from_next_month = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][1]//button[@class='rdr-MonthAndYear-button next']"
    
    # To date filter
    div_to_group = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][2]"
    lbl_to = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][2]/label"
    div_to_daterange = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][2]/div[@class='daterange-container']"
    inp_to_date = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][2]//input[@class='input-text datepicker']"
    spn_to_calendar = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][2]//span[@class='oi oi-calendar icon-calendar ml-1']"
    
    # To date calendar overlay
    div_to_overlay = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][2]//div[@class='overlay']"
    div_to_calendar = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][2]//div[@class='rdr-Calendar']"
    btn_to_prev_month = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][2]//button[@class='rdr-MonthAndYear-button prev']"
    sel_to_month = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][2]//select[@class='rdr-MonthAndYearSelect'][1]"
    sel_to_year = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][2]//select[@class='rdr-MonthAndYearSelect'][2]"
    btn_to_next_month = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][2]//button[@class='rdr-MonthAndYear-button next']"
    
    # Get All checkbox
    div_get_all_group = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][3]"
    lbl_get_all = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][3]//label[@class='form-check-label']"
    chk_get_all = "//div[@class='filter-container']/div[@class='form-inline']/div[@class='mr-sm-2 form-group'][3]//input[@name='isGetAll']"
    
    # Search button
    btn_search = "//div[@class='filter-container']/div[@class='form-inline']/button[@class='btn btn-outline-primary']"
    spn_search_icon = "//div[@class='filter-container']/div[@class='form-inline']/button[@class='btn btn-outline-primary']/span[@class='oi oi-magnifying-glass']"
    
    # Statement History section
    div_statement_history = "//div[@class='data-content statement-history']"
    div_table_responsive = "//div[@class='data-content statement-history']/div[@class='table-responsive table-striped my-2']"
    div_table_container = "//div[@class='data-content statement-history']//div[@class='table-container']"
    
    # Header section
    div_header_content = "//div[@class='data-content statement-history']//div[@class='header-content']"
    tbl_header = "//div[@class='data-content statement-history']//div[@class='header-content']//table"
    
    # Header columns
    th_number = "//div[@class='data-content statement-history']//div[@class='header-content']//th[1]"
    th_date = "//div[@class='data-content statement-history']//div[@class='header-content']//th[2]"
    th_type = "//div[@class='data-content statement-history']//div[@class='header-content']//th[3]"
    th_amount = "//div[@class='data-content statement-history']//div[@class='header-content']//th[4]"
    th_status = "//div[@class='data-content statement-history']//div[@class='header-content']//th[5]"
    th_creator = "//div[@class='data-content statement-history']//div[@class='header-content']//th[6]"
    th_description = "//div[@class='data-content statement-history']//div[@class='header-content']//th[7]"
    
    # Body section
    div_body_content = "//div[@class='data-content statement-history']//div[@class='body-content']"
    tbl_body = "//div[@class='data-content statement-history']//div[@class='body-content']//table"
    
    # Dynamic methods for rows and cells
    @staticmethod
    def tr_statement_by_index(index):
        return f"//div[@class='data-content statement-history']//div[@class='body-content']//table//tbody/tr[{index + 1}]"
    
    @staticmethod
    def td_number_by_index(index):
        return f"//div[@class='data-content statement-history']//div[@class='body-content']//table//tbody/tr[{index + 1}]/td[1]"
    
    @staticmethod
    def td_date_by_index(index):
        return f"//div[@class='data-content statement-history']//div[@class='body-content']//table//tbody/tr[{index + 1}]/td[2]"
        
    @staticmethod
    def btn_month_toggle_by_index(index):
        return f"//div[@class='data-content statement-history']//div[@class='body-content']//table//tbody/tr[{index + 1}]/td[2]//button[@class='p-0 th-wrapper btn btn-link']"
    
    @staticmethod
    def td_type_by_index(index):
        return f"//div[@class='data-content statement-history']//div[@class='body-content']//table//tbody/tr[{index + 1}]/td[3]"
    
    @staticmethod
    def td_amount_by_index(index):
        return f"//div[@class='data-content statement-history']//div[@class='body-content']//table//tbody/tr[{index + 1}]/td[4]"
    
    @staticmethod
    def btn_amount_by_index(index):
        return f"//div[@class='data-content statement-history']//div[@class='body-content']//table//tbody/tr[{index + 1}]/td[4]//button[@class='p-0 btn btn-link']"
    
    @staticmethod
    def td_status_by_index(index):
        return f"//div[@class='data-content statement-history']//div[@class='body-content']//table//tbody/tr[{index + 1}]/td[5]"
    
    @staticmethod
    def td_creator_by_index(index):
        return f"//div[@class='data-content statement-history']//div[@class='body-content']//table//tbody/tr[{index + 1}]/td[6]"
    
    @staticmethod
    def td_description_by_index(index):
        return f"//div[@class='data-content statement-history']//div[@class='body-content']//table//tbody/tr[{index + 1}]/td[7]" 