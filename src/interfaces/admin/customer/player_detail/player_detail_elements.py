class PlayerDetailElements:
    # Filter section elements
    # Product filter
    lbl_product = "//label[text()='Product']"
    btn_product_dropdown = "//div[@id='select-2']/button[@class='select-label']"
    inp_product_search = "//div[@id='select-2']//input[@name='inputOption']"
    
    # Base currency filter
    lbl_base_currency = "//label[text()='Base Currency']"
    sel_base_currency = "//select[@id='BaseCurrency']"
    
    # Currency multi-select filter
    lbl_currency = "//label[@for='Currency']"
    btn_currency_dropdown = "//div[@id='multiple-select-2']/button"
    chk_currency_all = "//input[@id='multiple-select-2-optionItemAll']"
    
    # Month picker
    lbl_month = "//label[text()='Month']"
    inp_month = "//input[@class='mp-form-input']"
    icn_calendar = "//span[@class='oi oi-calendar']"
    sel_year = "//select[@class='mp-select-year']"
    
    # Action buttons
    btn_search = "//button[contains(@class, 'btn-outline-primary')]"
    btn_export_excel = "//button[contains(@class, 'btn-excel')]"
    
    # Table elements - Headers
    tbl_player_detail = "//div[@class='table-responsive table-striped my-2 player-detail']//table"
    
    th_row_number = "//thead//th[text()='#']"
    th_username = "//thead//th[contains(@class, 'th')][1]//span[text()='User Name']"
    th_system_name = "//thead//th[contains(@class, 'th')][2]//span[text()='System Name']"
    th_registration_date = "//thead//th[contains(@class, 'th')][3]//span[text()='Registration Date']"
    th_fdm_date = "//thead//th[contains(@class, 'th')][4]//span[text()='FDM Date']"
    th_fdm_amount = "//thead//th[contains(@class, 'th')][5]//span[text()='FDM Amt']"
    th_turnover = "//thead//th[contains(@class, 'th')][6]//span[text()='Turnover']"
    th_ggr = "//thead//th[contains(@class, 'th')][7]//span[text()='GGR']"
    th_deposit = "//thead//th[contains(@class, 'th')][8]//span[text()='Deposit']"
    th_withdrawal = "//thead//th[contains(@class, 'th')][9]//span[text()='Withdrawal']"
    th_bonus = "//thead//th[contains(@class, 'th')][10]//span[text()='Bonus']"
    th_rebate = "//thead//th[contains(@class, 'th')][11]//span[text()='Rebate']"
    th_deposit_fee = "//thead//th[contains(@class, 'th')][12]//span[text()='Deposit Fee']"
    th_withdrawal_fee = "//thead//th[contains(@class, 'th')][13]//span[text()='Withdrawal Fee']"
    
    # Sort icons
    icn_asc = "//span[@class='caret asc']"
    icn_desc = "//span[@class='caret desc']"
    icn_desc_current = "//span[@class='caret desc current']"
    
    # Table body
    tbl_body = "//div[@class='body-content']//table//tbody"
    
    # Pagination controls
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
    def get_product_option(option_label):
        """Returns XPath for a specific product option"""
        return f"//div[@id='select-2']//span[@class='option-label' and text()='{option_label}']"
    
    @staticmethod
    def get_currency_checkbox(currency_code):
        """Returns XPath for a specific currency checkbox"""
        return f"//span[@class='option-label' and text()='{currency_code}']/preceding-sibling::input"
    
    @staticmethod
    def get_month_button(month_name):
        """Returns XPath for a specific month button"""
        return f"//button[@class='mp-btn-month' and text()='{month_name}']"
    
    @staticmethod
    def get_row_by_username(username):
        """Returns XPath for a row with the specified username"""
        return f"//div[@class='body-content']//td[text()='{username}']/parent::tr"
    
    @staticmethod
    def get_cell_by_row_and_column(row_number, column_index):
        """Returns XPath for a specific cell by row number and column index"""
        return f"//div[@class='body-content']//tbody/tr[{row_number}]/td[{column_index}]"
