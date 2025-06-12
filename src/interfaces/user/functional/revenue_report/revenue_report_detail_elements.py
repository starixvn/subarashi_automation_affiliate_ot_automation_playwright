class RevenueReportDetailElements:

    # Detail rows container (all rows that are not summary or total)
    tr_detail = "//table[@id='dataTable']/tbody[@id='reportData']/tr[not(contains(@class, 'sumrow')) and not(contains(@class, 'total'))]"
    
    # Expanded detail rows
    tr_expanded = "//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'expanded')]"
    
    # Collapsed detail rows
    tr_collapsed = "//table[@id='dataTable']/tbody[@id='reportData']/tr[not(contains(@class, 'expanded')) and not(contains(@class, 'sumrow')) and not(contains(@class, 'total'))]"
    
    # Product names from the example
    div_product_ow_sports = "//div[contains(text(), 'OW Sports')]"
    div_product_ow_number_game = "//div[contains(text(), 'OW Number Game')]"
    div_product_ow_virtual_sports = "//div[contains(text(), 'OW Virtual Sports')]"
    div_product_sbsw_virtual_sports = "//div[contains(text(), 'SBSW Virtual Sports')]"
    div_product_v8_poker = "//div[contains(text(), 'V8 Poker')]"
    div_product_sg_rng = "//div[contains(text(), 'SG RNG')]" 