"""
Table Header Elements

This file contains XPath locators for the table header elements.
"""

class TableHeaderElements:
    """
    Class containing XPath locators for table header elements.
    """
    
    # Header row
    tr_header = "//table[@id='player-detail-table']/thead/tr[@class='player-detail-table-header']"
    
    # Basic header cells
    th_no = "//table[@id='player-detail-table']/thead/tr/th[1]" # No. column
    th_username = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Username']" # Username column
    th_registered_date = "//table[@id='player-detail-table']/thead/tr/th[@data-name='RegisteredDate']" # Registered Date column
    th_fdm_date = "//table[@id='player-detail-table']/thead/tr/th[@data-name='FdmDate']" # FDM Date column
    th_fdm_amt = "//table[@id='player-detail-table']/thead/tr/th[@data-name='FdmAmt']" # FDM Amt column
    th_turnover = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Turnover']" # Turnover column
    th_ggr = "//table[@id='player-detail-table']/thead/tr/th[@data-name='GGR']" # GGR column
    th_deposit = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Deposit']" # Deposited column
    th_withdrawal = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Withdrawal']" # Withdrawal column
    th_bonus = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Bonus']" # Bonus column
    th_rebate = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Rebate']" # Rebate column
    th_deposit_fee = "//table[@id='player-detail-table']/thead/tr/th[@data-name='DepositFee']" # Deposit Fee column
    th_withdrawal_fee = "//table[@id='player-detail-table']/thead/tr/th[@data-name='WithdrawalFee']" # Withdrawal Fee column
    
    # Header components
    div_th_wrapper_base = "//table[@id='player-detail-table']/thead/tr/th/div[@class='th-wrapper']"
    span_column_title_base = "//table[@id='player-detail-table']/thead/tr/th/div[@class='th-wrapper']/span"
    div_icon_container_base = "//table[@id='player-detail-table']/thead/tr/th/div[@class='th-wrapper']/div[@class='icon-container']"
    span_caret_asc_base = "//table[@id='player-detail-table']/thead/tr/th/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret asc']"
    span_caret_desc_base = "//table[@id='player-detail-table']/thead/tr/th/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret desc']"
    
    # Default sorting
    span_default_sorting = "//table[@id='player-detail-table']/thead/tr/th/div[@class='th-wrapper']/div[@class='icon-container']/span[@id='defaultSorting']"
    span_current_sort = "//table[@id='player-detail-table']/thead/tr/th/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret desc current']"
    
    # Username column components
    div_th_wrapper_username = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Username']/div[@class='th-wrapper']"
    span_column_title_username = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Username']/div[@class='th-wrapper']/span"
    div_icon_container_username = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Username']/div[@class='th-wrapper']/div[@class='icon-container']"
    span_caret_asc_username = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Username']/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret asc']"
    span_caret_desc_username = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Username']/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret desc']"
    
    # FDM Amt column components (default sorting)
    div_th_wrapper_fdm_amt = "//table[@id='player-detail-table']/thead/tr/th[@data-name='FdmAmt']/div[@class='th-wrapper']"
    span_column_title_fdm_amt = "//table[@id='player-detail-table']/thead/tr/th[@data-name='FdmAmt']/div[@class='th-wrapper']/span"
    div_icon_container_fdm_amt = "//table[@id='player-detail-table']/thead/tr/th[@data-name='FdmAmt']/div[@class='th-wrapper']/div[@class='icon-container']"
    span_caret_asc_fdm_amt = "//table[@id='player-detail-table']/thead/tr/th[@data-name='FdmAmt']/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret asc']"
    span_caret_desc_fdm_amt = "//table[@id='player-detail-table']/thead/tr/th[@data-name='FdmAmt']/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret desc current']"
    span_default_sorting_fdm_amt = "//table[@id='player-detail-table']/thead/tr/th[@data-name='FdmAmt']/div[@class='th-wrapper']/div[@class='icon-container']/span[@id='defaultSorting'][@class='caret desc current']"
    
    # Turnover column components
    div_th_wrapper_turnover = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Turnover']/div[@class='th-wrapper']"
    span_column_title_turnover = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Turnover']/div[@class='th-wrapper']/span"
    div_icon_container_turnover = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Turnover']/div[@class='th-wrapper']/div[@class='icon-container']"
    span_caret_asc_turnover = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Turnover']/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret asc']"
    span_caret_desc_turnover = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Turnover']/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret desc']"
    span_default_sorting_turnover = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Turnover']/div[@class='th-wrapper']/div[@class='icon-container']/span[@id='defaultSorting']"
    
    @staticmethod
    def get_header_cell_by_name(data_name):
        """
        Get the XPath for a specific header cell by its data-name attribute.
        
        Args:
            data_name (str): The data-name attribute value (Username, RegisteredDate, FdmDate, etc.).
            
        Returns:
            str: XPath locator for the specified header cell.
        """
        return f"//table[@id='player-detail-table']/thead/tr/th[@data-name='{data_name}']"
    
    @staticmethod
    def get_header_cell_title_by_name(data_name):
        """
        Get the XPath for a specific header cell title span by data-name attribute.
        
        Args:
            data_name (str): The data-name attribute value (Username, RegisteredDate, FdmDate, etc.).
            
        Returns:
            str: XPath locator for the title span of the specified header cell.
        """
        return f"//table[@id='player-detail-table']/thead/tr/th[@data-name='{data_name}']/div[@class='th-wrapper']/span"
    
    @staticmethod
    def get_sort_asc_by_column_name(data_name):
        """
        Get the XPath for the ascending sort icon of a specific column by data-name attribute.
        
        Args:
            data_name (str): The data-name attribute value (Username, RegisteredDate, FdmDate, etc.).
            
        Returns:
            str: XPath locator for the ascending sort icon of the specified column.
        """
        return f"//table[@id='player-detail-table']/thead/tr/th[@data-name='{data_name}']/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret asc']"
    
    @staticmethod
    def get_sort_desc_by_column_name(data_name):
        """
        Get the XPath for the descending sort icon of a specific column by data-name attribute.
        
        Args:
            data_name (str): The data-name attribute value (Username, RegisteredDate, FdmDate, etc.).
            
        Returns:
            str: XPath locator for the descending sort icon of the specified column.
        """
        return f"//table[@id='player-detail-table']/thead/tr/th[@data-name='{data_name}']/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret desc']"
    
    @staticmethod
    def get_current_sort_by_column_name(data_name):
        """
        Get the XPath for the current sort icon of a specific column by data-name attribute.
        
        Args:
            data_name (str): The data-name attribute value (Username, RegisteredDate, FdmDate, etc.).
            sort_direction (str): The sort direction ('asc' or 'desc').
            
        Returns:
            str: XPath locator for the current sort icon of the specified column.
        """
        return f"//table[@id='player-detail-table']/thead/tr/th[@data-name='{data_name}']/div[@class='th-wrapper']/div[@class='icon-container']/span[contains(@class, 'current')]" 