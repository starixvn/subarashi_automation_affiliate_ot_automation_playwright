"""
Power Block Elements

This file contains XPath locators for the power block elements on the Affiliate page.
"""

class PowerBlockElements:
    """
    Class containing XPath locators for the power block elements.
    """
    
    # Block container
    div_block_power = "//div[@class='block block-power']"
    div_page_container = "//div[@class='block block-power']/div[@class='page-container']"
    div_group_page = "//div[@class='block block-power']/div[@class='page-container']/div[@class='group-page']"
    
    # Block title and description
    div_block_child_title = "//div[@class='block block-power']//div[@class='block-child-title']"
    div_block_child_description = "//div[@class='block block-power']//div[@class='block-child-description']"
    
    # Table elements
    div_table_custom = "//div[@class='block block-power']//div[@class='table-custom table-responsive']"
    table = "//div[@class='block block-power']//div[@class='table-custom table-responsive']/table"
    thead = "//div[@class='block block-power']//div[@class='table-custom table-responsive']/table/thead"
    tbody = "//div[@class='block block-power']//div[@class='table-custom table-responsive']/table/tbody"
    
    # Table header cells
    th_fdm = "//div[@class='block block-power']//table/thead/tr/th[1]"
    th_deposit = "//div[@class='block block-power']//table/thead/tr/th[2]"
    th_commission = "//div[@class='block block-power']//table/thead/tr/th[3]"
    th_max_commission = "//div[@class='block block-power']//table/thead/tr/th[4]"
    
    # Table rows
    tr_first = "//div[@class='block block-power']//table/tbody/tr[1]"
    tr_second = "//div[@class='block block-power']//table/tbody/tr[2]"
    tr_third = "//div[@class='block block-power']//table/tbody/tr[3]"
    tr_fourth = "//div[@class='block block-power']//table/tbody/tr[4]"
    
    @staticmethod
    def get_row_by_index(index=1):
        """
        Get the XPath for a specific table row by index.
        
        Args:
            index (int): The index of the row (1-based).
            
        Returns:
            str: XPath locator for the specified row.
        """
        return f"//div[@class='block block-power']//table/tbody/tr[{index}]"
    
    @staticmethod
    def get_cell_by_row_and_column(row_index=1, col_index=1):
        """
        Get the XPath for a specific table cell by row and column index.
        
        Args:
            row_index (int): The index of the row (1-based).
            col_index (int): The index of the column (1-based).
            
        Returns:
            str: XPath locator for the specified cell.
        """
        return f"//div[@class='block block-power']//table/tbody/tr[{row_index}]/td[{col_index}]" 