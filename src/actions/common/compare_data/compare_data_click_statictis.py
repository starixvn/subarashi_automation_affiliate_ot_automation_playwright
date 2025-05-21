from config.constants.settings import *
env = ENVIRONMENT
import time

from src.actions.common.get_data_on_function.get_data_customer import GetDataCustomer
from src.test_data.common.data_common import *
from src.interfaces.admin.customer.statistics_elements import StatisticsElements as elm_statistics
from src.interfaces.admin.customer.submenu_elements import SubmenuElements as elm_submenu
from src.interfaces.admin.customer.left_panel_elements import LeftPanelElements as elm_left_panel
from src.interfaces.admin.customer.click_statistics.referrers_elements import ReferrersElements as elm_referrers
from src.interfaces.admin.customer.click_statistics.landing_pages_elements import LandingPagesElements as elm_landing_pages
from src.interfaces.admin.customer.click_statistics.marketing_page_elements import MarketingPageElements as elm_marketing_page
from src.interfaces.admin.customer.click_statistics.submenu_elements import SubmenuElements as elm_submenu_click_statistics
from src.interfaces.admin.common.common_elements import CommonElements as elm_common
from src.interfaces.admin.common.header_elements import HeaderElements as elm_header
from src.interfaces.admin.common.menu_elements import MenuElements as elm_menu

from src.test_data.common.data_click_statistics.data_referrers.data_referrers_last_month import DataReferrersLastMonth
from src.test_data.common.data_click_statistics.data_referrers.data_referrers_last_week import DataReferrersLastWeek
from src.test_data.common.data_click_statistics.data_referrers.data_referrers_yesterday import DataReferrersYesterday
from src.test_data.common.data_click_statistics.data_referrers.data_referrers_last_month_by_desktop import DataReferrersLastMonthByDesktop
from src.test_data.common.data_click_statistics.data_referrers.data_referrers_last_week_by_desktop import DataReferrersLastWeekByDesktop
from src.test_data.common.data_click_statistics.data_referrers.data_referrers_yesterday_by_desktop import DataReferrersYesterdayByDesktop
from src.test_data.common.data_click_statistics.data_referrers.data_referrers_last_month_by_mobile import DataReferrersLastMonthByMobile
from src.test_data.common.data_click_statistics.data_referrers.data_referrers_last_week_by_mobile import DataReferrersLastWeekByMobile
from src.test_data.common.data_click_statistics.data_referrers.data_referrers_yesterday_by_mobile import DataReferrersYesterdayByMobile

Data = {
    "TestCase_spread_sheet_id": TestCase_Spread_Sheet_Id,
    "TestCase_Auto_Status": TestCase_Auto_Status,
    "Referres_Last_Month" : DataReferrersLastMonth.data_referrers_last_month,
    "Referres_Last_Week" : DataReferrersLastWeek.data_referrers_last_week,
    "Referres_Yesterday" : DataReferrersYesterday.data_referrers_yesterday,
    "Referres_Last_Month_By_Desktop" : DataReferrersLastMonthByDesktop.data_referrers_last_month_by_desktop,
    "Referres_Last_Week_By_Desktop" : DataReferrersLastWeekByDesktop.data_referrers_last_week_by_desktop,
    "Referres_Yesterday_By_Desktop" : DataReferrersYesterdayByDesktop.data_referrers_yesterday_by_desktop,
    "Referres_Last_Month_By_Mobile" : DataReferrersLastMonthByMobile.data_referrers_last_month_by_mobile,
    "Referres_Last_Week_By_Mobile" : DataReferrersLastWeekByMobile.data_referrers_last_week_by_mobile,
    "Referres_Yesterday_By_Mobile" : DataReferrersYesterdayByMobile.data_referrers_yesterday_by_mobile,
}
Checklist_Sheet_Name = "Compare_Data_Clickstatistics"


class CompareDataClickStatistics(GetDataCustomer):
    def __init__(self):
        super().__init__()
        self.get_data_customer = GetDataCustomer()

    def check_data_referrers_in_customer(self, testcase):
            subAutoTestCase = ''
            mainChecklist = ["Verify that the Referrers data displayed is correct according to the date picker.",
                         "Verify that the Referrers data displayed is correct by device.",
                         "Verify that the Referrers data in the \"Click Statistics\" sub‑function matches the data in Statistics.",
                         "Verify that the Total Clicks for Referrers equal the Total Clicks for Landing Pages.",
                         "Verify that the Total Clicks for Referrers equal the Total Clicks for Marketing Pages.",
                         "Verify that the Signups for Referrers equal the Signups for Landing Pages.",
                         "Verify that the Signups for Referrers equal the Signups for Marketing Pages.",
                         "Verify that the FDM for Referrers equals the FDM for Landing Pages.",
                         "Verify that the FDM for Referrers equals the FDM for Marketing Pages.",
                         "Verify that when clicking on a Page (if not None), the sub‑data table is displayed.",
                         "Verify that the values in the sub‑data table match the corresponding row in the main table.",
                         "Verify that the total Signups for the month equal the total Signups in the Statistics data table.",
                         "Verify that the total FDM for the month equals the total Signups in the Statistics data table.",
                         "Verify that if there is data in the Total Clicks column, then the Unique Click column also contains data."
                        ]
            indexChl = 0
            try:
                subAutoTestCase = subAutoTestCase + '- Verify that the data displayed is correct according to the last month'

                username = Data["Referres_Last_Month"]["metadata"]["filters"]["username"]
                device_type = Data["Referres_Last_Month"]["metadata"]["filters"]["device_type"]
                from_date = Data["Referres_Last_Month"]["metadata"]["period"]["from_date"]
                to_date = Data["Referres_Last_Month"]["metadata"]["period"]["to_date"]
                
                data_referrers_in_customer = self.get_data_referrers_in_customer(username,from_date,to_date,device_type)
                
                self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0],sheet_name=Checklist_Sheet_Name)
                indexChl = indexChl + 1 
                subAutoTestCase = ""
            except Exception as e:
                self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][1],sheet_name=Checklist_Sheet_Name)
                indexChl = indexChl + 1
                if indexChl < len(mainChecklist):
                    for i in range(indexChl, len(mainChecklist)):
                        if i >= len(mainChecklist):
                            break
                        self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, "", Data["TestCase_Auto_Status"][2],sheet_name=Checklist_Sheet_Name)
                self.utils.page.extract_TestCaseFailed(e)
            
        
