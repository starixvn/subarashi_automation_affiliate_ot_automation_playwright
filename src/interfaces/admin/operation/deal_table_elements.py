"""
Deal Table Elements - Absolute Stable XPath mappings for 12BetAdmin2 Portal Operation
Based on actual HTML structure analysis from live site - NO data-ref dependencies
Production-ready element mappings with multiple fallback strategies
"""

class DealTableElements:
    """
    Deal Table Elements - Complete stable XPath mapping for Deal table operations
    """
    
    # ========== PAGE STRUCTURE & NAVIGATION ==========
    # Root container
    div_root_container = "//div[@id='root']"
    
    # Operation navigation
    img_operation_icon = "//img[contains(@src, 'i_operation.png')]"
    lnk_operation_tab = "//a[@id='Operation' and contains(@href, '/Portal/Operation')]"
    lnk_deal_tab = "//a[@aria-current='page' and contains(@href, '/Portal/Operation')]"
    
    # ========== SEARCH FORM SECTION ==========
    # Deal Name field - STABLE by ID and name
    lbl_deal_name = "//label[@for='DealName']"
    inp_deal_name = "//input[@id='DealName']"
    inp_deal_name_by_name = "//input[@name='DealName']"
    inp_deal_name_by_class = "//input[contains(@class, 'search-box')][@type='text']"
    
    # Deal Type dropdown - STABLE by ID and name  
    lbl_deal_type = "//label[@for='DealType']"
    sel_deal_type = "//select[@id='DealType']"
    sel_deal_type_by_name = "//select[@name='DealType']"
    sel_deal_type_by_class = "//select[contains(@class, 'search-box')]"
    
    # Deal Type options - STABLE by value and text
    opt_all_types = "//select[@name='DealType']/option[@value='0']"
    opt_all_types_text = "//select[@name='DealType']/option[text()='All Types']"
    opt_cpa = "//select[@name='DealType']/option[@value='3']" 
    opt_cpa_text = "//select[@name='DealType']/option[text()='CPA']"
    opt_hybrid = "//select[@name='DealType']/option[@value='4']"
    opt_hybrid_text = "//select[@name='DealType']/option[text()='Hybrid CPA/Revenue Share']"
    opt_revenue_share = "//select[@name='DealType']/option[@value='1']"
    opt_revenue_share_text = "//select[@name='DealType']/option[text()='Revenue Share']"
    
    # Search button - STABLE by content and structure
    btn_search = "//button[@type='button' and contains(., 'Search')]"
    btn_search_with_icon = "//button[.//span[contains(@class, 'oi-magnifying-glass')]]"
    btn_search_in_form = "//div[@class='form-inline']//button[contains(., 'Search')]"
    
    # ========== ACTION BUTTONS ==========
    # Add Deal button - STABLE by content and structure
    btn_add_deal = "//button[@type='button' and contains(., 'Add Deal')]"
    btn_add_deal_with_icon = "//button[.//span[contains(@class, 'oi-plus')]]"
    btn_add_deal_by_class = "//button[contains(@class, 'btn-outline-secondary')]"
    
    # ========== TABLE STRUCTURE ==========
    # Table container - STABLE by class and structure
    div_table_container = "//div[@class='table-responsive table-striped']"
    div_header_content = "//div[@class='header-content']"
    div_body_content = "//div[@class='body-content']"
    
    # Table elements - STABLE by HTML structure
    tbl_header = "//div[@class='header-content']//table[@class='table']"
    tbl_body = "//div[@class='body-content']//table[@class='table']"
    thead_main = "//table[@class='table']/thead"
    tbody_main = "//table[@class='table']/tbody"
    
    # Table headers - STABLE by text content
    th_number = "//table//th[text()='#']"
    th_deal_name = "//table//th[text()='Deal Name']"
    th_deal_type = "//table//th[text()='Deal Type']"
    th_no_aff = "//table//th[text()='No.Aff']"
    th_description = "//table//th[text()='Description']"
    th_updated_by = "//table//th[text()='Updated By']"
    th_updated_date = "//table//th[text()='Updated Date']"
    th_action = "//table//th[text()='Action']"
    
    # Table rows - STABLE by structure (excluding first empty row)
    tr_all_data_rows = "//table[@class='table']/tbody/tr[position()>1]"
    tr_data_rows_by_td = "//table[@class='table']/tbody/tr[td[@title]]"
    
    # Deal name buttons - STABLE by structure and class
    btns_deal_names = "//table/tbody/tr/td[2]//button[@type='button']"
    btns_deal_names_by_class = "//table/tbody/tr/td//button[contains(@class, 'btn-link')][@type='button']"
    
    # No.Aff links - STABLE by href pattern
    lnks_no_aff = "//table/tbody/tr/td/a[contains(@href, '/Portal/Affiliate?groupId=')]"
    lnks_no_aff_by_target = "//table/tbody/tr/td/a[@target='_top']"
    
    # Action buttons - STABLE by title attribute
    btns_copy = "//table/tbody/tr/td/button[@title='Copy']"
    btns_copy_by_icon = "//table/tbody/tr/td/button[.//span[contains(@class, 'icon-copy-link')]]"
    btns_delete = "//table/tbody/tr/td/button[@title='Delete']"
    btns_delete_by_icon = "//table/tbody/tr/td/button[.//span[contains(@class, 'oi-x')]]"
    btns_delete_disabled = "//table/tbody/tr/td/button[@disabled and @title='Delete']"
    
    # ========== PAGINATION SECTION ==========
    # Pagination container - STABLE by class and content
    div_pagination = "//div[@class='page-container center-align']"
    div_page_input = "//div[@class='page-input']"
    
    # Page navigation links - STABLE by class and href
    lnk_first_page = "//a[@class='icon page-first disable']"
    lnk_first_page_active = "//a[@class='icon page-first ']"
    lnk_prev_page = "//a[@class='icon page-prev disable']"
    lnk_prev_page_active = "//a[@class='icon page-prev ']"
    lnk_next_page = "//a[@class='icon page-next ']"
    lnk_next_page_disable = "//a[@class='icon page-next disable']"
    lnk_last_page = "//a[@class='icon page-last ']"
    lnk_last_page_disable = "//a[@class='icon page-last disable']"
    
    # Page input - STABLE by class and attributes
    inp_page_number = "//input[@class='page-form']"
    inp_page_number_by_attr = "//input[@type='text' and @maxlength='4' and @size='2']"
    
    # Page size dropdown - STABLE by class
    sel_page_size = "//select[@class='pagesize-select']"
    
    # Page size options - STABLE by value
    opt_page_size_10 = "//select[@class='pagesize-select']/option[@value='10']"
    opt_page_size_20 = "//select[@class='pagesize-select']/option[@value='20']"
    opt_page_size_50 = "//select[@class='pagesize-select']/option[@value='50']"
    opt_page_size_100 = "//select[@class='pagesize-select']/option[@value='100']"
    opt_page_size_200 = "//select[@class='pagesize-select']/option[@value='200']"
    opt_page_size_500 = "//select[@class='pagesize-select']/option[@value='500']"
    
    # Pagination info - STABLE by class and content pattern
    span_page_info = "//span[@class='page-info']"
    span_view_info = "//span[contains(text(), 'View') and contains(text(), 'of')]"
    span_page_text = "//span[contains(text(), 'Page') and contains(text(), 'of')]"
    
    # ========== HIDDEN FORM ELEMENTS ==========
    # CSRF token - STABLE by name
    inp_csrf_token = "//input[@name='__RequestVerificationToken']"
    inp_root_url = "//input[@id='RootUrl']"
    iframe_session = "//iframe[contains(@src, '/Portal/Auth/ReCheckIn')]"
    
    # ========== DYNAMIC HELPER METHODS ==========
    @staticmethod
    def get_deal_name_button_by_text(deal_name):
        """Get deal name button by exact text - STABLE"""
        return f"//table/tbody/tr/td[2]//button[@type='button' and text()='{deal_name}']"
    
    @staticmethod
    def get_deal_name_button_by_row(row_number):
        """Get deal name button by row number (1-based, excluding first empty row) - STABLE"""
        actual_row = row_number + 1  # Skip first empty row
        return f"//table[@class='table']/tbody/tr[{actual_row}]/td[2]//button[@type='button']"
    
    @staticmethod
    def get_table_cell_by_row_column(row_number, column_number):
        """Get table cell by row and column number (1-based) - STABLE"""
        actual_row = row_number + 1  # Skip first empty row
        return f"//table[@class='table']/tbody/tr[{actual_row}]/td[{column_number}]"
    
    @staticmethod
    def get_table_cell_by_title(title_text):
        """Get table cell by title attribute - STABLE"""
        return f"//table/tbody/tr/td[@title='{title_text}']"
    
    @staticmethod
    def get_copy_button_by_row(row_number):
        """Get copy button by row number - STABLE"""
        actual_row = row_number + 1
        return f"//table[@class='table']/tbody/tr[{actual_row}]/td/button[@title='Copy']"
    
    @staticmethod
    def get_delete_button_by_row(row_number):
        """Get delete button by row number - STABLE"""
        actual_row = row_number + 1
        return f"//table[@class='table']/tbody/tr[{actual_row}]/td/button[@title='Delete']"
    
    @staticmethod
    def get_no_aff_link_by_row(row_number):
        """Get No.Aff link by row number - STABLE"""
        actual_row = row_number + 1
        return f"//table[@class='table']/tbody/tr[{actual_row}]/td/a[contains(@href, '/Portal/Affiliate?groupId=')]"
    
    @staticmethod
    def get_no_aff_link_by_group_id(group_id):
        """Get No.Aff link by group ID - STABLE"""
        return f"//table/tbody/tr/td/a[@href='/12BetAdmin2/Portal/Affiliate?groupId={group_id}']"
    
    @staticmethod
    def get_deal_type_option_by_value(value):
        """Get deal type option by value - STABLE"""
        return f"//select[@name='DealType']/option[@value='{value}']"
    
    @staticmethod
    def get_deal_type_option_by_text(text):
        """Get deal type option by text - STABLE"""
        return f"//select[@name='DealType']/option[text()='{text}']"
    
    @staticmethod
    def get_page_size_option_by_value(value):
        """Get page size option by value - STABLE"""
        return f"//select[@class='pagesize-select']/option[@value='{value}']"
    
    @staticmethod
    def get_table_row_by_deal_name(deal_name):
        """Get entire table row by deal name - STABLE"""
        return f"//table/tbody/tr[td[2]//button[@type='button' and text()='{deal_name}']]"
    
    @staticmethod
    def get_table_data_by_deal_name_and_column(deal_name, column_number):
        """Get specific column data for a deal by name - STABLE"""
        return f"//table/tbody/tr[td[2]//button[@type='button' and text()='{deal_name}']]/td[{column_number}]"
    
    @staticmethod
    def get_action_button_by_deal_name(deal_name, action_title):
        """Get action button (Copy/Delete) by deal name and title - STABLE"""
        return f"//table/tbody/tr[td[2]//button[@type='button' and text()='{deal_name}']]/td/button[@title='{action_title}']"
    
    @staticmethod
    def get_table_row_by_position(position):
        """Get table row by position (1-based, excluding first row) - STABLE"""
        actual_row = position + 1
        return f"//table[@class='table']/tbody/tr[{actual_row}]"
    
    @staticmethod
    def get_deal_data_by_column_title(deal_name, column_title):
        """Get deal data by column title - STABLE"""
        column_map = {
            '#': 1, 'Deal Name': 2, 'Deal Type': 3, 'No.Aff': 4,
            'Description': 5, 'Updated By': 6, 'Updated Date': 7, 'Action': 8
        }
        column_number = column_map.get(column_title, 1)
        return f"//table/tbody/tr[td[2]//button[@type='button' and text()='{deal_name}']]/td[{column_number}]"
    
    # ========== MULTIPLE FALLBACK STRATEGIES ==========
    @staticmethod
    def get_search_button_all_strategies():
        """Multiple strategies for search button - HIGHEST RELIABILITY"""
        return [
            "//button[@type='button' and contains(., 'Search')]",
            "//button[.//span[contains(@class, 'oi-magnifying-glass')]]",
            "//div[@class='form-inline']//button[contains(., 'Search')]",
            "//label[@for='DealName']/..//button[contains(., 'Search')]"
        ]
    
    @staticmethod
    def get_add_deal_button_all_strategies():
        """Multiple strategies for add deal button - HIGHEST RELIABILITY"""
        return [
            "//button[@type='button' and contains(., 'Add Deal')]",
            "//button[.//span[contains(@class, 'oi-plus')]]",
            "//button[contains(@class, 'btn-outline-secondary')]",
            "//div[@class='data-content']//button[contains(., 'Add Deal')]"
        ]
    
    @staticmethod
    def get_deal_name_input_all_strategies():
        """Multiple strategies for deal name input - HIGHEST RELIABILITY"""
        return [
            "//input[@id='DealName']",
            "//input[@name='DealName']",
            "//input[contains(@class, 'search-box')][@type='text']",
            "//label[@for='DealName']/..//input[@type='text']"
        ]
    
    @staticmethod
    def get_deal_type_select_all_strategies():
        """Multiple strategies for deal type select - HIGHEST RELIABILITY"""
        return [
            "//select[@id='DealType']",
            "//select[@name='DealType']",
            "//select[contains(@class, 'search-box')]",
            "//label[@for='DealType']/..//select"
        ]
    
    @staticmethod
    def get_page_size_dropdown_all_strategies():
        """Multiple strategies for page size dropdown - HIGHEST RELIABILITY"""
        return [
            "//select[@class='pagesize-select']",
            "//div[@class='page-container center-align']//select",
            "//select[option[@value='10'] and option[@value='20'] and option[@value='50']]",
            "//span[@class='page-info']/..//select"
        ]
    
    @staticmethod
    def get_pagination_container_all_strategies():
        """Multiple strategies for pagination container - HIGHEST RELIABILITY"""
        return [
            "//div[@class='page-container center-align']",
            "//div[.//span[@class='page-info']]",
            "//div[.//input[@class='page-form']]",
            "//div[contains(., 'View') and contains(., 'of')]"
        ]
    
    @staticmethod
    def get_table_container_all_strategies():
        """Multiple strategies for table container - HIGHEST RELIABILITY"""
        return [
            "//div[@class='table-responsive table-striped']",
            "//div[@class='table-container']",
            "//div[.//table[@class='table']]",
            "//div[.//th[text()='Deal Name']]"
        ]
    
    @staticmethod
    def verify_deal_table_loaded():
        """Verify deal table is properly loaded - STABLE CHECK"""
        return [
            "//table//th[text()='Deal Name']",
            "//table//th[text()='Deal Type']", 
            "//table//th[text()='Action']",
            "//div[@class='page-container center-align']"
        ] 