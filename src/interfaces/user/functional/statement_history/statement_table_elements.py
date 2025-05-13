class StatementTableElements:
    """
    Class containing XPath locators for the Statement Table elements.
    These elements are for the main statement data table.
    """

    # Table container elements
    div_table_responsive = "//div[@id='statementDataList']/div[@class='table table-responsive']"
    table = "//div[@id='statementDataList']//table"
    
    # Table header elements
    thead = "//div[@id='statementDataList']//table/thead"
    tr_header = "//div[@id='statementDataList']//table/thead/tr"
    th_empty = "//div[@id='statementDataList']//table/thead/tr/th[1]"
    th_date = "//div[@id='statementDataList']//table/thead/tr/th[2]"
    th_media_type = "//div[@id='statementDataList']//table/thead/tr/th[3]"
    th_amount = "//div[@id='statementDataList']//table/thead/tr/th[4]"
    th_status = "//div[@id='statementDataList']//table/thead/tr/th[5]"
    th_description = "//div[@id='statementDataList']//table/thead/tr/th[6]"
    
    # Table body elements
    tbody = "//div[@id='statementDataList']//table/tbody"
    tr_row = "//div[@id='statementDataList']//table/tbody/tr"
    
    def get_row_by_id(self, row_id):
        """Get row by data-id attribute"""
        return f"//div[@id='statementDataList']//table/tbody/tr[@data-id='{row_id}']"
    
    def get_row_by_index(self, index):
        """Get row by index (1-based)"""
        return f"//div[@id='statementDataList']//table/tbody/tr[{index}]"
    
    def get_parent_row(self, row_id=None, index=None):
        """Get parent row by data-id or index"""
        if row_id:
            return f"//div[@id='statementDataList']//table/tbody/tr[@data-id='{row_id}' and @data-parent='']"
        elif index:
            return f"//div[@id='statementDataList']//table/tbody/tr[@data-parent=''][{index}]"
        else:
            return "//div[@id='statementDataList']//table/tbody/tr[@data-parent='']"
    
    def get_child_row(self, parent_id):
        """Get child row by parent data-id"""
        return f"//div[@id='statementDataList']//table/tbody/tr[@data-parent='{parent_id}']"
    
    def get_cell(self, row_id, column_index):
        """Get cell by row data-id and column index (1-based)"""
        return f"//div[@id='statementDataList']//table/tbody/tr[@data-id='{row_id}']/td[{column_index}]"
    
    def get_row_number(self, row_id):
        """Get row number (1st column) by row data-id"""
        return f"//div[@id='statementDataList']//table/tbody/tr[@data-id='{row_id}']/td[1]"
    
    def get_row_date(self, row_id):
        """Get row date (2nd column) by row data-id"""
        return f"//div[@id='statementDataList']//table/tbody/tr[@data-id='{row_id}']/td[2]"
    
    def get_row_media_type(self, row_id):
        """Get row media type (3rd column) by row data-id"""
        return f"//div[@id='statementDataList']//table/tbody/tr[@data-id='{row_id}']/td[3]"
    
    def get_row_amount(self, row_id):
        """Get row amount (4th column) by row data-id"""
        return f"//div[@id='statementDataList']//table/tbody/tr[@data-id='{row_id}']/td[4]"
    
    def get_row_status(self, row_id):
        """Get row status (5th column) by row data-id"""
        return f"//div[@id='statementDataList']//table/tbody/tr[@data-id='{row_id}']/td[5]"
    
    def get_row_description(self, row_id):
        """Get row description (6th column) by row data-id"""
        return f"//div[@id='statementDataList']//table/tbody/tr[@data-id='{row_id}']/td[6]"
    
    def get_expand_button(self, row_id):
        """Get expand/collapse button for a row"""
        return f"//div[@id='statementDataList']//table/tbody/tr[@data-id='{row_id}']//button[@class='btn btn-transparent']"
    
    def get_chevron_indicator(self, row_id):
        """Get chevron indicator (right/bottom) for a row"""
        return f"//div[@id='statementDataList']//table/tbody/tr[@data-id='{row_id}']//span[contains(@class, 'chevron')]"
    
    def get_amount_link(self, row_id):
        """Get amount link element by row data-id"""
        return f"//div[@id='statementDataList']//table/tbody/tr[@data-id='{row_id}']//a[@class='amountItem']"
    
    def get_rows_by_status(self, status):
        """Get all rows with specific status text"""
        return f"//div[@id='statementDataList']//table/tbody/tr[./td[5][contains(text(), '{status}')]]"
    
    def get_rows_by_media_type(self, media_type):
        """Get all rows with specific media type text"""
        return f"//div[@id='statementDataList']//table/tbody/tr[./td[3][contains(text(), '{media_type}')]]" 