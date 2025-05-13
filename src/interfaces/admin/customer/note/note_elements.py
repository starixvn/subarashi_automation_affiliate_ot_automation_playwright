class NoteElements:
    """
    Note page element selectors for the admin interface.
    
    Follows these criteria:
    - Each XPath selector targets a unique element
    - Uses IDs and unique classes where available
    - Avoids selectors that rely on text content
    - Follows a clear DOM structure
    """
    # Action Buttons
    btn_add_note = "//button[@class='btn btn-outline-secondary']"
    spn_add_icon = "//button[@class='btn btn-outline-secondary']/span[@class='oi oi-plus ml-2']"
    
    # Table structure
    div_table_responsive = "//div[@class='table-responsive table-striped my-2']"
    div_table_container = "//div[@class='table-container']"
    
    # Table header
    div_header_content = "//div[@class='header-content']"
    tbl_header = "//div[@class='header-content']//table"
    th_number = "//div[@class='header-content']//th[1]"
    th_content = "//div[@class='header-content']//th[2]"
    th_created_by = "//div[@class='header-content']//th[3]"
    th_last_modify = "//div[@class='header-content']//th[4]"
    th_edit = "//div[@class='header-content']//th[5]"
    
    # Table body
    div_body_content = "//div[@class='body-content']"
    tbl_body = "//div[@class='body-content']//table"
    
    # Dynamic method for note row by index (1-based)
    @staticmethod
    def tr_note_by_index(index):
        return f"//div[@class='body-content']//table//tr[{index + 1}]"
    
    # Dynamic method for content cell by index
    @staticmethod
    def td_content_by_index(index):
        return f"//div[@class='body-content']//table//tr[{index + 1}]/td[2]"
    
    # Dynamic method for creator cell by index
    @staticmethod
    def td_creator_by_index(index):
        return f"//div[@class='body-content']//table//tr[{index + 1}]/td[3]"
    
    # Dynamic method for last modify cell by index
    @staticmethod
    def td_last_modify_by_index(index):
        return f"//div[@class='body-content']//table//tr[{index + 1}]/td[4]"
    
    # Dynamic method for edit button by index
    @staticmethod
    def btn_edit_by_index(index):
        return f"//div[@class='body-content']//table//tr[{index + 1}]//button[@class='p-0 btn btn-link']"
    
    # Dynamic method for edit icon by index
    @staticmethod
    def spn_edit_icon_by_index(index):
        return f"//div[@class='body-content']//table//tr[{index + 1}]//span[@class='oi oi-pencil text-secondary']"
    
    # Pagination controls
    div_pagination = "//div[@class='page-container center-align']"
    lnk_first_page = "//div[@class='page-container center-align']/a[@class='icon page-first']"
    lnk_prev_page = "//div[@class='page-container center-align']/a[@class='icon page-prev']"
    div_page_input = "//div[@class='page-container center-align']/div[@class='page-input']"
    inp_page_number = "//div[@class='page-container center-align']//input[@class='page-form']"
    spn_total_pages = "//div[@class='page-container center-align']/div[@class='page-input']/span[2]"
    lnk_next_page = "//div[@class='page-container center-align']/a[@class='icon page-next']"
    lnk_last_page = "//div[@class='page-container center-align']/a[@class='icon page-last']"
    sel_page_size = "//div[@class='page-container center-align']/select[@class='pagesize-select']"
    spn_page_info = "//div[@class='page-container center-align']/span[@class='page-info']"
    
    # Dynamic method for page size option
    @staticmethod
    def opt_page_size_by_value(size_value):
        return f"//select[@class='pagesize-select']/option[@value='{size_value}']" 