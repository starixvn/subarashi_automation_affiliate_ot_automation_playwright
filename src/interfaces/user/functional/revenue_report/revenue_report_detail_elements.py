class RevenueReportDetailElements:
    """
    Class containing XPath locators for the Revenue Report detail rows.
    These elements are for the expandable detail rows with product-specific information.
    """

    # Detail rows container (all rows that are not summary or total)
    tr_detail = "//table[@id='dataTable']/tbody[@id='reportData']/tr[not(contains(@class, 'sumrow')) and not(contains(@class, 'total'))]"
    
    # Expanded detail rows
    tr_expanded = "//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'expanded')]"
    
    # Collapsed detail rows
    tr_collapsed = "//table[@id='dataTable']/tbody[@id='reportData']/tr[not(contains(@class, 'expanded')) and not(contains(@class, 'sumrow')) and not(contains(@class, 'total'))]"
    
    # Detail row cells (for a specific product - should be used with proper row selector)
    td_empty = ".//td[1]"  # First column is empty in detail rows
    td_product = ".//td[2]"  # Product name cell
    td_turnover = ".//td[3]"  # Turnover cell
    td_ggr = ".//td[4]"  # GGR cell
    
    # Product names from the example
    div_product_ow_sports = "//div[contains(text(), 'OW Sports')]"
    div_product_ow_number_game = "//div[contains(text(), 'OW Number Game')]"
    div_product_ow_virtual_sports = "//div[contains(text(), 'OW Virtual Sports')]"
    div_product_sbsw_virtual_sports = "//div[contains(text(), 'SBSW Virtual Sports')]"
    div_product_v8_poker = "//div[contains(text(), 'V8 Poker')]"
    div_product_sg_rng = "//div[contains(text(), 'SG RNG')]"
    
    def get_detail_rows_for_month(self, month):
        """Get all detail rows for a specific month"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][.//div[contains(text(), '{month}')]]/following-sibling::tr[not(contains(@class, 'sumrow')) and not(contains(@class, 'total'))]"
    
    def get_expanded_rows_for_month(self, month):
        """Get expanded detail rows for a specific month"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][.//div[contains(text(), '{month}')]]/following-sibling::tr[contains(@class, 'expanded')]"
    
    def get_product_row(self, product):
        """Get row for a specific product"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[.//div[contains(text(), '{product}')]]"
    
    def get_product_turnover(self, product):
        """Get turnover for a specific product"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[.//div[contains(text(), '{product}')]]/td[3]"
    
    def get_product_ggr(self, product):
        """Get GGR for a specific product"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[.//div[contains(text(), '{product}')]]/td[4]"
    
    def get_month_products(self, month):
        """Get all products for a specific month"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][.//div[contains(text(), '{month}')]]/following-sibling::tr[not(contains(@class, 'sumrow')) and not(contains(@class, 'total'))]//div[@class='row-wrapper']"
    
    def get_detail_row_by_index(self, month_index, product_index):
        """Get specific detail row by month index and product index within that month (both 1-based)"""
        month_xpath = f"//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][{month_index}]"
        return f"({month_xpath}/following-sibling::tr[not(contains(@class, 'sumrow')) and not(contains(@class, 'total'))])[{product_index}]"
    
    def get_detail_turnover_by_index(self, month_index, product_index):
        """Get turnover for specific detail row by month index and product index (both 1-based)"""
        detail_row = self.get_detail_row_by_index(month_index, product_index)
        return f"{detail_row}/td[3]"
    
    def get_detail_ggr_by_index(self, month_index, product_index):
        """Get GGR for specific detail row by month index and product index (both 1-based)"""
        detail_row = self.get_detail_row_by_index(month_index, product_index)
        return f"{detail_row}/td[4]"
    
    def count_products_for_month(self, month):
        """Count number of products for a specific month"""
        return f"count(//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][.//div[contains(text(), '{month}')]]/following-sibling::tr[not(contains(@class, 'sumrow')) and not(contains(@class, 'total'))])"
    
    def toggle_details_for_month(self, month):
        """Get chevron element to toggle details for a specific month"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][.//div[contains(text(), '{month}')]]//span[@class='chevron toggleDetailRow']" 