class PlayerElements:
    """
    Element selectors for the Player page in the admin interface.
    
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
    div_filter_container = "//div[@class='filter-container my-2']"
    div_form_inline = "//div[@class='filter-container my-2']/div[@class='form-inline']"
    
    # Affiliate filter
    lbl_affiliate = "//div[@class='filter-container my-2']//label[text()='Affiliate']"
    inp_affiliate = "//div[@class='filter-container my-2']//input[@name='affName']"
    
    # User Name filter
    lbl_username = "//div[@class='filter-container my-2']//label[text()='User Name']"
    inp_username = "//div[@class='filter-container my-2']//input[@name='userName']"
    
    # System Name filter
    lbl_system_name = "//div[@class='filter-container my-2']//label[text()='System Name']"
    inp_system_name = "//div[@class='filter-container my-2']//input[@name='ibcUserName']"

    # Include Removed Players filter
    lbl_include_removed_players = "//div[@class='filter-container my-2']//label[text()='Include removed Players']"
    chk_include_removed_players = "//div[@class='filter-container my-2']//label[text()='Include removed Players']//input[@type='checkbox']"
    
    # Search button
    btn_search = "//div[@class='filter-container my-2']//button[@class='btn btn-outline-primary']"
    icon_search = "//div[@class='filter-container my-2']//span[@class='oi oi-magnifying-glass']"
    
    # Main content area
    div_data_content = "//div[@class='data-content']"
    div_member_list = "//div[@class='member-list-content table-responsive table-striped my-2']"
    
    # Table container
    div_table_container = "//div[@class='table-container']"
    div_header_content = "//div[@class='header-content']"
    div_body_content = "//div[@class='body-content']"
    
    # Table headers - first row (main headers)
    tbl_header = "//div[@class='header-content']//table"
    tr_first_row = "//div[@class='header-content']//tr[@class='first-row']"
    tr_header_main = "//div[@class='header-content']//tr[2]"
    th_number = "//div[@class='header-content']//th[@title='#']"
    th_username = "//div[@class='header-content']//th[@title='User Name']"
    th_system_name = "//div[@class='header-content']//th[@title='System Name']"
    th_first_name = "//div[@class='header-content']//th[@title='First Name']"
    th_last_name = "//div[@class='header-content']//th[@title='Last Name']"
    th_registration_date = "//div[@class='header-content']//th[@title='Registration Date']"
    th_affiliate = "//div[@class='header-content']//th[@title='Affiliate']"
    th_removed = "//div[@class='header-content']//th[@title='Removed']"
    
    # Table headers - second row (sub-headers)
    tr_header_sub = "//div[@class='header-content']//tr[3]"
    th_status = "//div[@class='header-content']//tr[3]/th[@title='Status']"
    th_last_action_date = "//div[@class='header-content']//tr[3]/th[@title='Last Action Date']"
    th_edit = "//div[@class='header-content']//tr[3]/th[@title='Edit']"
    
    # Table body
    tbl_body = "//div[@class='body-content']//table"
    tr_body_first_row = "//div[@class='body-content']//tr[@class='first-row']"
    
    # No data message
    td_no_data = "//div[@class='body-content']//td[@class='text-center' and @colspan='10']"
    
    # Pagination section
    div_page_container = "//div[@class='page-container center-align']"
    lnk_page_first = "//a[@class='icon page-first disable']"
    lnk_page_prev = "//a[@class='icon page-prev disable']"
    div_page_input = "//div[@class='page-input']"
    inp_page = "//input[@class='page-form']"
    spn_page_total = "//div[@class='page-input']/span[2]"
    lnk_page_next = "//a[@class='icon page-next disable']"
    lnk_page_last = "//a[@class='icon page-last']"
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
    def tr_by_row_index(index):
        return f"//div[@class='body-content']//tbody/tr[{index + 1}]"
    
    @staticmethod
    def td_number_by_row_index(index):
        return f"//div[@class='body-content']//tbody/tr[{index + 1}]/td[1]"
    
    @staticmethod
    def td_username_by_row_index(index):
        return f"//div[@class='body-content']//tbody/tr[{index + 1}]/td[2]"
    
    @staticmethod
    def td_system_name_by_row_index(index):
        return f"//div[@class='body-content']//tbody/tr[{index + 1}]/td[3]"
    
    @staticmethod
    def td_first_name_by_row_index(index):
        return f"//div[@class='body-content']//tbody/tr[{index + 1}]/td[4]"
    
    @staticmethod
    def td_last_name_by_row_index(index):
        return f"//div[@class='body-content']//tbody/tr[{index + 1}]/td[5]"
    
    @staticmethod
    def td_registration_date_by_row_index(index):
        return f"//div[@class='body-content']//tbody/tr[{index + 1}]/td[6]"
    
    @staticmethod
    def td_affiliate_by_row_index(index):
        return f"//div[@class='body-content']//tbody/tr[{index + 1}]/td[7]"
    
    @staticmethod
    def td_status_by_row_index(index):
        return f"//div[@class='body-content']//tbody/tr[{index + 1}]/td[8]"
    
    @staticmethod
    def td_last_action_date_by_row_index(index):
        return f"//div[@class='body-content']//tbody/tr[{index + 1}]/td[9]"
    
    @staticmethod
    def td_edit_by_row_index(index):
        return f"//div[@class='body-content']//tbody/tr[{index + 1}]/td[10]"
    
    @staticmethod
    def lnk_edit_by_row_index(index):
        return f"//div[@class='body-content']//tbody/tr[{index + 1}]/td[10]/a"
    
    @staticmethod
    def tr_by_username(username):
        return f"//div[@class='body-content']//td[2][contains(@title, '{username}')]/parent::tr" 