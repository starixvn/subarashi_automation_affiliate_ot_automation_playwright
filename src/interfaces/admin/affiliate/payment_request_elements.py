class PaymentRequestElements:
    """
    Element selectors for the Payment Request page in the admin interface.
    
    Follows these criteria:
    - Each XPath selector targets a unique element
    - Uses IDs and unique classes where available
    - Avoids selectors that rely on text content where possible
    - Follows a clear DOM structure
    - Simple and direct XPath without unnecessary conditions
    """
    # Loader elements
    div_loader = "//div[@class='loader']"
    div_backdrop = "//div[@class='backdrop']"
    div_spinner = "//div[@class='spinner']"
    
    # Filter section
    div_filter_container = "//div[@class='filter-container']"
    
    # Search By dropdown
    lbl_search_by = "//div[@class='filter-container']//label[text()='Search By']"
    sel_search_by = "//div[@class='filter-container']//select[@name='searchBy']"
    opt_username = "//div[@class='filter-container']//select[@name='searchBy']/option[@value='1']"
    opt_others = "//div[@class='filter-container']//select[@name='searchBy']/option[@value='2']"
    
    # Username field
    lbl_username = "//div[@class='filter-container']//label[text()='User Name']"
    inp_username = "//div[@class='filter-container']//input[@name='userName']"
    
    # Search button
    btn_search = "//div[@class='filter-container']//button[@class='btn btn-outline-primary']"
    icon_search = "//div[@class='filter-container']//span[@class='oi oi-magnifying-glass']"
    
    # Main content area
    div_data_content = "//div[@class='data-content payment-request']"
    
    # Table container
    div_table_responsive = "//div[@class='table-responsive table-striped my-2']"
    div_table_container = "//div[@class='table-container']"
    div_header_content = "//div[@class='header-content']"
    div_body_content = "//div[@class='body-content']"
    
    # Table headers
    tbl_header = "//div[@class='header-content']//table"
    th_number = "//div[@class='header-content']//th[@title='#']"
    th_transaction_id = "//div[@class='header-content']//th[@title='Trxn.ID']"
    th_requested_date = "//div[@class='header-content']//th[@title='Requested Date']"
    th_username = "//div[@class='header-content']//th[@title='User Name']"
    th_amount = "//div[@class='header-content']//th[@title='Amount']"
    th_status = "//div[@class='header-content']//th[@title='Status']"
    th_completed_date = "//div[@class='header-content']//th[@title='Completed Date']"
    th_creator = "//div[@class='header-content']//th[@title='Creator']"
    
    # Table body
    tbl_body = "//div[@class='body-content']//table"
    
    # First row cells (approved status row)
    tr_first_row = "//div[@class='body-content']//tr[@class='approved'][1]"
    td_row_number_1 = "//div[@class='body-content']//tr[@class='approved'][1]/td[@title='1']"
    td_transaction_id_1 = "//div[@class='body-content']//tr[@class='approved'][1]/td[@title='1450']"
    btn_transaction_id_1 = "//div[@class='body-content']//tr[@class='approved'][1]/td[@title='1450']/button"
    td_requested_date_1 = "//div[@class='body-content']//tr[@class='approved'][1]/td[@title='03/06/2025 16:46:15']"
    td_username_1 = "//div[@class='body-content']//tr[@class='approved'][1]/td[@title='12BETAFF030']"
    td_amount_1 = "//div[@class='body-content']//tr[@class='approved'][1]/td[@title='100.00']"
    td_status_1 = "//div[@class='body-content']//tr[@class='approved'][1]/td[@title='Approved']"
    td_completed_date_1 = "//div[@class='body-content']//tr[@class='approved'][1]/td[@title='03/06/2025 16:48:31']"
    td_creator_1 = "//div[@class='body-content']//tr[@class='approved'][1]/td[@title='AANina']"
    
    # Second row cells
    tr_second_row = "//div[@class='body-content']//tr[@class='approved'][2]"
    td_row_number_2 = "//div[@class='body-content']//tr[@class='approved'][2]/td[@title='2']"
    td_transaction_id_2 = "//div[@class='body-content']//tr[@class='approved'][2]/td[@title='1687']"
    btn_transaction_id_2 = "//div[@class='body-content']//tr[@class='approved'][2]/td[@title='1687']/button"
    td_requested_date_2 = "//div[@class='body-content']//tr[@class='approved'][2]/td[@title='01/06/2025 16:46:15']"
    td_username_2 = "//div[@class='body-content']//tr[@class='approved'][2]/td[@title='12BETAFF030']"
    td_amount_2 = "//div[@class='body-content']//tr[@class='approved'][2]/td[@title='100.00']"
    td_status_2 = "//div[@class='body-content']//tr[@class='approved'][2]/td[@title='Approved']"
    td_completed_date_2 = "//div[@class='body-content']//tr[@class='approved'][2]/td[@title='03/06/2025 16:48:31']"
    td_creator_2 = "//div[@class='body-content']//tr[@class='approved'][2]/td[8][@class='text-center']"
    
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
    def tr_row_by_status_and_index(status, index):
        return f"//div[@class='body-content']//tr[@class='{status}'][{index}]"
    
    @staticmethod
    def td_number_by_row_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[1][@class='text-center']"
    
    @staticmethod
    def td_transaction_id_by_row_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[2][@class='text-center']"
    
    @staticmethod
    def btn_transaction_id_by_row_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[2]/button"
    
    @staticmethod
    def td_requested_date_by_row_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[3][@class='text-center']"
    
    @staticmethod
    def td_username_by_row_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[4][@class='text-center']"
    
    @staticmethod
    def td_amount_by_row_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[5][@class='text-right']"
    
    @staticmethod
    def td_status_by_row_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[6][@class='text-center text-capitalize']"
    
    @staticmethod
    def td_completed_date_by_row_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[7][@class='text-center']"
    
    @staticmethod
    def td_creator_by_row_index(index):
        return f"//div[@class='body-content']//tr[{index}]/td[8][@class='text-center']"
    
    @staticmethod
    def tr_by_transaction_id(transaction_id):
        return f"//div[@class='body-content']//td[@title='{transaction_id}']/parent::tr" 