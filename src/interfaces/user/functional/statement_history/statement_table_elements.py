class StatementTableElements:

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