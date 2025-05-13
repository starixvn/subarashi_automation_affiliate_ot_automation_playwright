class SubMenuElements:
    # Container elements
    div_sub_menu = "//div[@class='sub-menu-container']"
    div_image = "//div[@class='d-inline-block'][1]"
    img_admin = "//img[@src='/12BetAdmin3/Areas/Portal/www/dist/imgs/i_admin.png']"
    div_nav = "//div[@class='d-inline-block'][2]"
    
    # Navigation elements
    ul_nav = "//ul[@class='nav']"
    li_admin_list = "//li[@class='nav-item'][1]"
    lnk_admin_list = "//a[@class='nav-link' and contains(@href, '/Administrator')]"
    lnk_admin_list_active = "//a[@class='nav-link active' and contains(@href, '/Administrator')]"
    
    li_dept_list = "//li[@class='nav-item'][2]"
    lnk_dept_list = "//a[@class='nav-link' and contains(@href, '/Department')]"
    lnk_dept_list_active = "//a[@class='nav-link active' and contains(@href, '/Department')]"
    
    # Helper methods to check active state
    def is_admin_list_active(self):
        return "//a[contains(@href, '/Administrator') and contains(@class, 'active')]"
    
    def is_dept_list_active(self):
        return "//a[contains(@href, '/Department') and contains(@class, 'active')]" 