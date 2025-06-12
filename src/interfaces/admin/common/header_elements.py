class HeaderElements:
    # Header container
    div_header = "//header[@class='header']"
    div_header_wrapper = "//header[@class='header']/div[@class='headWrapper']"
    
    # Logo
    div_logo = "//div[@class='headWrapper']/div[@class='float-left logo']"
    img_logo = "//div[@class='float-left logo']/img"
    
    # User info section
    div_user_info = "//div[@class='headWrapper']/div[@class='float-left user-info']"
    spn_welcome_user = "//div[@class='float-left user-info']/span[@class='font-weight-bold icon-top']"
    lnk_change_password = "//div[@class='float-left user-info']/a[@class='text-redlink btn-changePassword']"
    lnk_logout = "//div[@class='float-left user-info']/a[@class='text-redlink btn-logout']"
    
    # Clock section
    div_clock_container = "//div[@class='headWrapper']/div[@class='float-right clock-container']"
    spn_clock_icon = "//div[@class='float-right clock-container']/span[@class='oi oi-clock']"
    spn_clock = "//div[@class='float-right clock-container']/span[@id='clock']"
    
    # Dynamic selector to get username from welcome message
    @staticmethod
    def get_username_xpath():
        """Returns XPath to extract the username from the welcome message"""
        return "//div[@class='float-left user-info']/span[@class='font-weight-bold icon-top']/text()"
