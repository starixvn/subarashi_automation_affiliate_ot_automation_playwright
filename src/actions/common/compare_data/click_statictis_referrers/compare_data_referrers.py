from config.constants.settings import *
env = ENVIRONMENT
import random
from datetime import datetime, timedelta

from src.actions.common.get_data_on_function.get_data_customer import GetDataCustomer
from src.test_data.common.data_common import *
from src.actions.common.get_data_on_function.get_data_player import GetDataPlayer

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


class CompareDataReferrers(GetDataCustomer):
    def __init__(self):
        super().__init__()
        self.get_data_customer = GetDataCustomer()

    def _compare_site_urls(self, baseline_site_urls, current_site_urls):
        """So sánh site URLs giữa baseline và dữ liệu hiện tại"""
        if len(baseline_site_urls) != len(current_site_urls):
            raise Exception(f"Number of site URLs mismatch. Baseline: {len(baseline_site_urls)}, Current: {len(current_site_urls)}")
        
        for site_url, baseline_site_data in baseline_site_urls.items():
            site_found = False
            for current_site in current_site_urls:
                if current_site["site_url"] == site_url:
                    site_found = True
                    if int(current_site["total_click"]) != baseline_site_data["total_clicks"]:
                        raise Exception(f"Total clicks mismatch for site {site_url}. Baseline: {baseline_site_data['total_clicks']}, Current: {current_site['total_click']}")
                    if int(current_site["unique_click"]) != baseline_site_data["unique_clicks"]:
                        raise Exception(f"Unique clicks mismatch for site {site_url}. Baseline: {baseline_site_data['unique_clicks']}, Current: {current_site['unique_click']}")
                    if int(current_site["signups"]) != baseline_site_data["signups"]:
                        raise Exception(f"Signups mismatch for site {site_url}. Baseline: {baseline_site_data['signups']}, Current: {current_site['signups']}")
                    if int(current_site["fdm"]) != baseline_site_data["fdm"]:
                        raise Exception(f"FDM mismatch for site {site_url}. Baseline: {baseline_site_data['fdm']}, Current: {current_site['fdm']}")
                    break
            
            if not site_found and site_url.lower() != "none":
                raise Exception(f"Site URL '{site_url}' not found in current data")
    
    def _compare_website_urls(self, baseline_website_urls_data, current_website_urls_data):
        """So sánh website URLs giữa baseline và dữ liệu hiện tại"""
        for site_url, baseline_website_urls in baseline_website_urls_data.items():
            if site_url.lower() == "none":
                continue
            
            if site_url not in current_website_urls_data:
                raise Exception(f"Website URLs for site '{site_url}' not found in current data")
            
            current_website_urls = current_website_urls_data[site_url]
            
            if len(baseline_website_urls) != len(current_website_urls):
                raise Exception(f"Number of website URLs mismatch for site {site_url}. Baseline: {len(baseline_website_urls)}, Current: {len(current_website_urls)}")
            
            for baseline_website in baseline_website_urls:
                website_found = False
                for current_website in current_website_urls:
                    if current_website["website_url"] == baseline_website["website_url"]:
                        website_found = True
                        if int(current_website["total_clicks"]) != baseline_website["total_clicks"]:
                            raise Exception(f"Total clicks mismatch for website {baseline_website['website_url']}. Baseline: {baseline_website['total_clicks']}, Current: {current_website['total_clicks']}")
                        if int(current_website["unique_clicks"]) != baseline_website["unique_clicks"]:
                            raise Exception(f"Unique clicks mismatch for website {baseline_website['website_url']}. Baseline: {baseline_website['unique_clicks']}, Current: {current_website['unique_clicks']}")
                        if int(current_website["sign_up"]) != baseline_website["signups"]:
                            raise Exception(f"Signups mismatch for website {baseline_website['website_url']}. Baseline: {baseline_website['signups']}, Current: {current_website['sign_up']}")
                        if int(current_website["fdm"]) != baseline_website["fdm"]:
                            raise Exception(f"FDM mismatch for website {baseline_website['website_url']}. Baseline: {baseline_website['fdm']}, Current: {current_website['fdm']}")
                        break
                
                if not website_found:
                    raise Exception(f"Website URL '{baseline_website['website_url']}' not found in current data for site {site_url}")
    
    def parse_int(self, text):
                try:
                    return int(str(text).replace(',', '').strip() or 0)
                except (ValueError, TypeError):
                    return 0
            
    def parse_fraction(self, text):
        try:
            if '/' in str(text):
                parts = str(text).split('/')
                return {
                    "unique": self.parse_int(parts[0]),
                    "total": self.parse_int(parts[1]) if len(parts) > 1 else 0
                }
            return {"unique": 0, "total": 0}
        except Exception:
            return {"unique": 0, "total": 0}
    
    def _compare_referrers_with_page(self, period, device_type, page_type="landing"):
        """
        Compare Total Clicks between Referrers and Landing Pages/Marketing Pages
        """
        username = self._get_username()
        date_range = self._get_date_range(period)
        
        data_referrers = self.get_data_referrers_in_customer(username, date_range["from_date"], date_range["to_date"], device_type)
        
        referrers_total_clicks = 0
        if data_referrers.get("has_data", True):
            for site_data in data_referrers["site_urls_data"]:
                referrers_total_clicks += self.parse_int(site_data["total_click"])
        
        if page_type == "landing":
            data_pages = self.get_data_landing_pages_in_customer(username, "All", "All", date_range["from_date"], date_range["to_date"], device_type)
            pages_name = "Landing Pages"
            
            pages_total_clicks = 0
            if data_pages.get("has_data", True):
                for page in data_pages["pages_data"]:
                    pages_total_clicks += self.parse_int(page["total_click"])
        else:
            data_pages = self.get_data_marketing_pages_in_customer(username, "All", date_range["from_date"], date_range["to_date"], device_type)
            pages_name = "Marketing Pages"
            
            pages_total_clicks = 0
            if data_pages.get("has_data", True):
                for channel in data_pages["channels_data"]:
                    pages_total_clicks += self.parse_int(channel["total_click"])
        
        has_data = data_referrers.get("has_data", True) and data_pages.get("has_data", True)
        
        result = ""
        if has_data:
            result += f"\n     + Username: {username}"
            result += f"\n     + From Date: {date_range['from_date']}"
            result += f"\n     + To Date: {date_range['to_date']}"
            
            if referrers_total_clicks == pages_total_clicks:
                result += f"\n     + Total Clicks match: {referrers_total_clicks}"
            else:
                result += f"\n     + Total Clicks mismatch: Referrers={referrers_total_clicks}, {pages_name}={pages_total_clicks}"
        else:
            result += f"\n     + No data found for Total Clicks for Referrers or {pages_name}."
        
        return result

    def _get_username(self):
        if ENVIRONMENT == "local":
            return "12BETAFF001"
        else:
            self.data_player = GetDataPlayer()
            self.data_player.referUtils(self.utils)
            top_100_data_player = self.data_player.get_top_100_data_player()
            return top_100_data_player["players_data"][random.randint(0, len(top_100_data_player["players_data"]) - 1)]["affiliate_name"]
        
    def _get_date_range(self, period):
        today = datetime.now()
        
        if period == "last_month":
            first_day_current_month = today.replace(day=1)
            last_day_previous_month = first_day_current_month - timedelta(days=1)
            first_day_previous_month = last_day_previous_month.replace(day=1)
            from_date = first_day_previous_month.strftime("%m-%d-%Y")
            to_date = last_day_previous_month.strftime("%m-%d-%Y")
            month_date = last_day_previous_month.strftime("%m-%Y")
        else:
            first_day_current_month = today.replace(day=1)
            from_date = first_day_current_month.strftime("%m-%d-%Y")
            to_date = today.strftime("%m-%d-%Y")
            month_date = today.strftime("%m-%Y")
        
        return {
            "from_date": from_date,
            "to_date": to_date,
            "month_date": month_date
        }

    def _check_data_for_period_and_device(self, period, device_type):
        username = self._get_username()
        date_range = self._get_date_range(period)
        
        data_referrers = self.get_data_referrers_in_customer(username, date_range["from_date"], date_range["to_date"], device_type)
        data_statistics = self.get_data_statistics_in_customer(username, date_range["month_date"])
        
        new_signups_fdm = str(data_statistics["new_signups_month"]).split('/')
        statistics_signups = self.parse_int(new_signups_fdm[0])
        statistics_fdm = self.parse_int(new_signups_fdm[1]) if len(new_signups_fdm) > 1 else 0
        
        pc_tracking = self.parse_fraction(data_statistics["tracking_pc_month"])
        mobile_tracking = self.parse_fraction(data_statistics["tracking_mobile_month"])
        
        if device_type == "All":
            statistics_total_clicks = pc_tracking["total"] + mobile_tracking["total"]
            statistics_unique_clicks = pc_tracking["unique"] + mobile_tracking["unique"]
        elif device_type == "Mobile":
            statistics_total_clicks = mobile_tracking["total"]
            statistics_unique_clicks = mobile_tracking["unique"]
        else:
            statistics_total_clicks = pc_tracking["total"]
            statistics_unique_clicks = pc_tracking["unique"]
        
        referrers_total_clicks = 0
        referrers_unique_clicks = 0
        referrers_signups = 0
        referrers_fdm = 0
        
        if data_referrers.get("has_data", True):
            for site_data in data_referrers["site_urls_data"]:
                referrers_total_clicks += self.parse_int(site_data["total_click"])
                referrers_unique_clicks += self.parse_int(site_data["unique_click"])
                referrers_signups += self.parse_int(site_data["signups"])
                referrers_fdm += self.parse_int(site_data["fdm"])
        
        mismatches = []
        
        click_type = "Total Clicks"
        if device_type == "Mobile":
            click_type = "Mobile Total Clicks"
        elif device_type == "PC / Laptop":
            click_type = "Desktop Total Clicks"
        
        if referrers_total_clicks != statistics_total_clicks:
            mismatches.append(f"{click_type} mismatch: Statistics={statistics_total_clicks}, Referrers={referrers_total_clicks}")
        
        if referrers_signups != statistics_signups:
            mismatches.append(f"Signups mismatch: Statistics={statistics_signups}, Referrers={referrers_signups}")
        
        if referrers_fdm != statistics_fdm:
            mismatches.append(f"FDM mismatch: Statistics={statistics_fdm}, Referrers={referrers_fdm}")
        
        if mismatches:
            raise Exception("\n".join(mismatches))
        
        return {
            "username": username,
            "device_type": device_type,
            "from_date": date_range["from_date"],
            "to_date": date_range["to_date"],
            "statistics_total_clicks": statistics_total_clicks,
            "statistics_unique_clicks": statistics_unique_clicks,
            "referrers_total_clicks": referrers_total_clicks,
            "referrers_unique_clicks": referrers_unique_clicks,
            "statistics_signups": statistics_signups,
            "referrers_signups": referrers_signups,
            "statistics_fdm": statistics_fdm,
            "referrers_fdm": referrers_fdm,
            "click_type": click_type
        }

    def _format_test_results(self, results, device_display_name):
        formatted_result = ""
        formatted_result += f"\n     + Username: {results['username']}"
        formatted_result += f"\n     + Device Type: {results['device_type']}"
        formatted_result += f"\n     + From Date: {results['from_date']}"
        formatted_result += f"\n     + To Date: {results['to_date']}"
        
        if device_display_name == "All":
            formatted_result += f"\n     + Total Clicks: Statistics={results['statistics_total_clicks']}, Referrers={results['referrers_total_clicks']}"
            formatted_result += f"\n     + Unique Clicks: Statistics={results['statistics_unique_clicks']}, Referrers={results['referrers_unique_clicks']}"
        else:
            formatted_result += f"\n     + {device_display_name} Total Clicks: Statistics={results['statistics_total_clicks']}, Referrers={results['referrers_total_clicks']}"
        
        formatted_result += f"\n     + Signups: Statistics={results['statistics_signups']}, Referrers={results['referrers_signups']}"
        formatted_result += f"\n     + FDM: Statistics={results['statistics_fdm']}, Referrers={results['referrers_fdm']}"
        
        return formatted_result

    def check_data_referrers_filter_by_date_and_device(self, testcase):
        subAutoTestCase = ''
        mainChecklist = ["Verify that the Referrers data displayed is correct according to the date picker.",
                        "Verify that the Referrers data displayed is correct by device."
                        ]
        indexChl = 0
        try:
            if "Referres_Last_Month" not in Data or not Data["Referres_Last_Month"]:
                raise Exception("Baseline data not found. Please run the job to collect baseline data first.")
                
            # LAST MONTH
            baseline_data_last_month = Data["Referres_Last_Month"]
            subAutoTestCase = subAutoTestCase + '- Verify that the data displayed is correct according to the last month'
            
            username = baseline_data_last_month["metadata"]["filters"]["username"]
            device_type = baseline_data_last_month["metadata"]["filters"]["device_type"]
            from_date = baseline_data_last_month["metadata"]["period"]["from_date"]
            to_date = baseline_data_last_month["metadata"]["period"]["to_date"]
            
            current_data = self.get_data_referrers_in_customer(username, from_date, to_date, device_type)
            
            baseline_has_data = baseline_data_last_month["metadata"].get("has_data", True)
            current_has_data = current_data.get("has_data", True)
            
            if not baseline_has_data and not current_has_data:
                subAutoTestCase = subAutoTestCase + " (No data expected - verified no data is present)"
            elif not baseline_has_data and current_has_data:
                raise Exception(f"Baseline data has no results but current query returned data. This suggests a data inconsistency.")
            elif baseline_has_data and not current_has_data:
                raise Exception(f"No current data found for user {username} from {from_date} to {to_date} with device type {device_type}, but baseline data exists")
            else:
                self._compare_site_urls(baseline_data_last_month["site_urls_data"], current_data["site_urls_data"])
                self._compare_website_urls(baseline_data_last_month["website_urls_data"], current_data["website_urls_data"])

            # LAST WEEK
            subAutoTestCase = subAutoTestCase + '\n- Verify that the data displayed is correct according to the last week'
            baseline_data_last_week = Data["Referres_Last_Week"]
            username = baseline_data_last_week["metadata"]["filters"]["username"]
            device_type = baseline_data_last_week["metadata"]["filters"]["device_type"]
            from_date = baseline_data_last_week["metadata"]["period"]["from_date"]
            to_date = baseline_data_last_week["metadata"]["period"]["to_date"]
            current_data = self.get_data_referrers_in_customer(username, from_date, to_date, device_type)
            
            baseline_has_data = baseline_data_last_week["metadata"].get("has_data", True)
            current_has_data = current_data.get("has_data", True)

            if not baseline_has_data and not current_has_data:
                subAutoTestCase = subAutoTestCase + " (No data expected - verified no data is present)"
            elif not baseline_has_data and current_has_data:
                raise Exception(f"Baseline data has no results but current query returned data. This suggests a data inconsistency.")
            elif baseline_has_data and not current_has_data:
                raise Exception(f"No current data found for user {username} from {from_date} to {to_date} with device type {device_type}, but baseline data exists")
            else:
                self._compare_site_urls(baseline_data_last_week["site_urls_data"], current_data["site_urls_data"])
                self._compare_website_urls(baseline_data_last_week["website_urls_data"], current_data["website_urls_data"])

            # YESTERDAY
            subAutoTestCase = subAutoTestCase + '\n- Verify that the data displayed is correct according to the yesterday'
            baseline_data_yesterday = Data["Referres_Yesterday"]
            username = baseline_data_yesterday["metadata"]["filters"]["username"]
            device_type = baseline_data_yesterday["metadata"]["filters"]["device_type"]
            from_date = baseline_data_yesterday["metadata"]["period"]["from_date"]
            to_date = baseline_data_yesterday["metadata"]["period"]["to_date"]
            
            current_data = self.get_data_referrers_in_customer(username, from_date, to_date, device_type)
            
            baseline_has_data = baseline_data_yesterday["metadata"].get("has_data", True)
            current_has_data = current_data.get("has_data", True)

            if not baseline_has_data and not current_has_data:
                subAutoTestCase = subAutoTestCase + " (No data expected - verified no data is present)"
            elif not baseline_has_data and current_has_data:
                raise Exception(f"Baseline data has no results but current query returned data. This suggests a data inconsistency.")
            elif baseline_has_data and not current_has_data:
                raise Exception(f"No current data found for user {username} from {from_date} to {to_date} with device type {device_type}, but baseline data exists")
            else:
                self._compare_site_urls(baseline_data_yesterday["site_urls_data"], current_data["site_urls_data"])
                self._compare_website_urls(baseline_data_yesterday["website_urls_data"], current_data["website_urls_data"])
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            indexChl = indexChl + 1 
            subAutoTestCase = ""

            # LAST MONTH BY DESKTOP
            subAutoTestCase = subAutoTestCase + '- Verify that the data displayed is correct according to the last month by desktop'
            baseline_data_last_month_by_desktop = Data["Referres_Last_Month_By_Desktop"]
            username = baseline_data_last_month_by_desktop["metadata"]["filters"]["username"]
            device_type = baseline_data_last_month_by_desktop["metadata"]["filters"]["device_type"]
            from_date = baseline_data_last_month_by_desktop["metadata"]["period"]["from_date"]
            to_date = baseline_data_last_month_by_desktop["metadata"]["period"]["to_date"]
            
            current_data = self.get_data_referrers_in_customer(username, from_date, to_date, device_type)
            
            baseline_has_data = baseline_data_last_month_by_desktop["metadata"].get("has_data", True)
            current_has_data = current_data.get("has_data", True)

            if not baseline_has_data and not current_has_data:
                subAutoTestCase = subAutoTestCase + " (No data expected - verified no data is present)"
            elif not baseline_has_data and current_has_data:
                raise Exception(f"Baseline data has no results but current query returned data. This suggests a data inconsistency.")
            elif baseline_has_data and not current_has_data:
                raise Exception(f"No current data found for user {username} from {from_date} to {to_date} with device type {device_type}, but baseline data exists")
            else:
                self._compare_site_urls(baseline_data_last_month_by_desktop["site_urls_data"], current_data["site_urls_data"])
                self._compare_website_urls(baseline_data_last_month_by_desktop["website_urls_data"], current_data["website_urls_data"])

            # LAST WEEK BY DESKTOP
            subAutoTestCase = subAutoTestCase + '\n- Verify that the data displayed is correct according to the last week by desktop'
            baseline_data_last_week_by_desktop = Data["Referres_Last_Week_By_Desktop"]
            username = baseline_data_last_week_by_desktop["metadata"]["filters"]["username"]
            device_type = baseline_data_last_week_by_desktop["metadata"]["filters"]["device_type"]
            from_date = baseline_data_last_week_by_desktop["metadata"]["period"]["from_date"]
            to_date = baseline_data_last_week_by_desktop["metadata"]["period"]["to_date"]
            
            current_data = self.get_data_referrers_in_customer(username, from_date, to_date, device_type)
            
            baseline_has_data = baseline_data_last_week_by_desktop["metadata"].get("has_data", True)
            current_has_data = current_data.get("has_data", True)
            
            if not baseline_has_data and not current_has_data:
                subAutoTestCase = subAutoTestCase + " (No data expected - verified no data is present)"
            elif not baseline_has_data and current_has_data:
                raise Exception(f"Baseline data has no results but current query returned data. This suggests a data inconsistency.")
            elif baseline_has_data and not current_has_data:
                raise Exception(f"No current data found for user {username} from {from_date} to {to_date} with device type {device_type}, but baseline data exists")
            else:
                self._compare_site_urls(baseline_data_last_week_by_desktop["site_urls_data"], current_data["site_urls_data"])
                self._compare_website_urls(baseline_data_last_week_by_desktop["website_urls_data"], current_data["website_urls_data"])

            # YESTERDAY BY DESKTOP
            subAutoTestCase = subAutoTestCase + '\n- Verify that the data displayed is correct according to the yesterday by desktop'
            
            baseline_data_yesterday_by_desktop = Data["Referres_Yesterday_By_Desktop"]
            username = baseline_data_yesterday_by_desktop["metadata"]["filters"]["username"]
            device_type = baseline_data_yesterday_by_desktop["metadata"]["filters"]["device_type"]
            from_date = baseline_data_yesterday_by_desktop["metadata"]["period"]["from_date"]
            to_date = baseline_data_yesterday_by_desktop["metadata"]["period"]["to_date"]
            
            current_data = self.get_data_referrers_in_customer(username, from_date, to_date, device_type)
            
            baseline_has_data = baseline_data_yesterday_by_desktop["metadata"].get("has_data", True)
            current_has_data = current_data.get("has_data", True)
            
            if not baseline_has_data and not current_has_data:
                subAutoTestCase = subAutoTestCase + " (No data expected - verified no data is present)"
            elif not baseline_has_data and current_has_data:
                raise Exception(f"Baseline data has no results but current query returned data. This suggests a data inconsistency.")
            elif baseline_has_data and not current_has_data:
                raise Exception(f"No current data found for user {username} from {from_date} to {to_date} with device type {device_type}, but baseline data exists")
            else:
                self._compare_site_urls(baseline_data_yesterday_by_desktop["site_urls_data"], current_data["site_urls_data"])
                self._compare_website_urls(baseline_data_yesterday_by_desktop["website_urls_data"], current_data["website_urls_data"])

            # LAST MONTH BY MOBILE
            subAutoTestCase = subAutoTestCase + '\n- Verify that the data displayed is correct according to the last month by mobile'
            baseline_data_last_month_by_mobile = Data["Referres_Last_Month_By_Mobile"]
            username = baseline_data_last_month_by_mobile["metadata"]["filters"]["username"]
            device_type = baseline_data_last_month_by_mobile["metadata"]["filters"]["device_type"]
            from_date = baseline_data_last_month_by_mobile["metadata"]["period"]["from_date"]
            to_date = baseline_data_last_month_by_mobile["metadata"]["period"]["to_date"]
            
            current_data = self.get_data_referrers_in_customer(username, from_date, to_date, device_type)
            
            baseline_has_data = baseline_data_last_month_by_mobile["metadata"].get("has_data", True)
            current_has_data = current_data.get("has_data", True)
            
            if not baseline_has_data and not current_has_data:
                subAutoTestCase = subAutoTestCase + " (No data expected - verified no data is present)"
            elif not baseline_has_data and current_has_data:
                raise Exception(f"Baseline data has no results but current query returned data. This suggests a data inconsistency.")
            elif baseline_has_data and not current_has_data:
                raise Exception(f"No current data found for user {username} from {from_date} to {to_date} with device type {device_type}, but baseline data exists")
            else:
                self._compare_site_urls(baseline_data_last_month_by_mobile["site_urls_data"], current_data["site_urls_data"])
                self._compare_website_urls(baseline_data_last_month_by_mobile["website_urls_data"], current_data["website_urls_data"])

            # LAST WEEK BY MOBILE
            subAutoTestCase = subAutoTestCase + '\n- Verify that the data displayed is correct according to the last week by mobile'
            baseline_data_last_week_by_mobile = Data["Referres_Last_Week_By_Mobile"]
            username = baseline_data_last_week_by_mobile["metadata"]["filters"]["username"]
            device_type = baseline_data_last_week_by_mobile["metadata"]["filters"]["device_type"]
            from_date = baseline_data_last_week_by_mobile["metadata"]["period"]["from_date"]
            to_date = baseline_data_last_week_by_mobile["metadata"]["period"]["to_date"]
            
            current_data = self.get_data_referrers_in_customer(username, from_date, to_date, device_type)
            
            baseline_has_data = baseline_data_last_week_by_mobile["metadata"].get("has_data", True)
            current_has_data = current_data.get("has_data", True)
            
            if not baseline_has_data and not current_has_data:
                subAutoTestCase = subAutoTestCase + " (No data expected - verified no data is present)"
            elif not baseline_has_data and current_has_data:
                raise Exception(f"Baseline data has no results but current query returned data. This suggests a data inconsistency.")
            elif baseline_has_data and not current_has_data:
                raise Exception(f"No current data found for user {username} from {from_date} to {to_date} with device type {device_type}, but baseline data exists")
            else:
                self._compare_site_urls(baseline_data_last_week_by_mobile["site_urls_data"], current_data["site_urls_data"])
                self._compare_website_urls(baseline_data_last_week_by_mobile["website_urls_data"], current_data["website_urls_data"])

            # YESTERDAY BY MOBILE
            subAutoTestCase = subAutoTestCase + '\n- Verify that the data displayed is correct according to the yesterday by mobile'
            baseline_data_yesterday_by_mobile = Data["Referres_Yesterday_By_Mobile"]
            username = baseline_data_yesterday_by_mobile["metadata"]["filters"]["username"]
            device_type = baseline_data_yesterday_by_mobile["metadata"]["filters"]["device_type"]
            from_date = baseline_data_yesterday_by_mobile["metadata"]["period"]["from_date"]
            to_date = baseline_data_yesterday_by_mobile["metadata"]["period"]["to_date"]

            current_data = self.get_data_referrers_in_customer(username, from_date, to_date, device_type)
            
            baseline_has_data = baseline_data_yesterday_by_mobile["metadata"].get("has_data", True)
            current_has_data = current_data.get("has_data", True)
            
            if not baseline_has_data and not current_has_data:
                subAutoTestCase = subAutoTestCase + " (No data expected - verified no data is present)"
            elif not baseline_has_data and current_has_data:
                raise Exception(f"Baseline data has no results but current query returned data. This suggests a data inconsistency.")
            elif baseline_has_data and not current_has_data:
                raise Exception(f"No current data found for user {username} from {from_date} to {to_date} with device type {device_type}, but baseline data exists")
            else:
                self._compare_site_urls(baseline_data_yesterday_by_mobile["site_urls_data"], current_data["site_urls_data"])
                self._compare_website_urls(baseline_data_yesterday_by_mobile["website_urls_data"], current_data["website_urls_data"])
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0],sheet_name=Checklist_Sheet_Name)
            indexChl = indexChl + 1
            subAutoTestCase = ''

        except Exception as e:
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][1],sheet_name=Checklist_Sheet_Name)
            indexChl = indexChl + 1
            if indexChl < len(mainChecklist):
                for i in range(indexChl, len(mainChecklist)):
                    if i >= len(mainChecklist):
                        break
                    self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[i], testcase, "", Data["TestCase_Auto_Status"][2],sheet_name=Checklist_Sheet_Name)
            self.utils.page.extract_TestCaseFailed(e)

    def preload_all_data(self):
        periods = ["last_month", "last_week", "current_month"]
        device_types = ["All", "PC / Laptop", "Mobile"]
        stats_periods = ["last_month", "current_month"]
        
        cache = {
            "referrers": {},
            "landing_pages": {},
            "marketing_pages": {},
            "statistics": {}
        }
        
        username = self._get_username()
        print(f"Preloading data for username: {username}")
        
        for period in periods:
            date_range = self._get_date_range(period)
            cache[period] = {
                "date_range": date_range
            }
            
            print(f"Fetching data for period: {period}")
            
            data_marketing_pages = self.get_data_marketing_pages_in_customer(
                username, "All", date_range["from_date"], date_range["to_date"], get_detail=False
            )
            
            if period in stats_periods:
                cache["statistics"][period] = self.get_data_statistics_in_customer(
                    username, date_range["month_date"]
                )
            
            for device_type in device_types:
                key = f"{period}_{device_type}"
                
                data_referrers = self.get_data_referrers_in_customer(
                    username, date_range["from_date"], date_range["to_date"], device_type, get_detail=False
                )
                cache["referrers"][key] = data_referrers
                
                data_landing_pages = self.get_data_landing_pages_in_customer(
                    username, "All", "All", date_range["from_date"], date_range["to_date"], device_type, get_detail=False
                )
                cache["landing_pages"][key] = data_landing_pages

                cache["marketing_pages"][key] = data_marketing_pages
        
        print("All data preloaded successfully!")
        return cache, username

    def check_data_referrers_click_statistics_and_compare(self, testcase):

        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that the Referrers data in the \"Click Statistics\" sub‑function matches the data in Statistics.",
                        "Verify that the Total Clicks for Referrers equal the Total Clicks for Landing Pages.",
                        "Verify that the Total Clicks for Referrers equal the Total Clicks for Marketing Pages."
                        ]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            time_periods = ["last_month", "current_month"]
            device_types = [
                {"name": "All", "display_name": "All"},
                {"name": "Mobile", "display_name": "Mobile"},
                {"name": "PC / Laptop", "display_name": "Desktop"}
            ]
            
            for period in time_periods:
                for device in device_types:
                    if subAutoTestCase:
                        subAutoTestCase += '\n'
                    subAutoTestCase += f"- Verify that the data of Referrers {device['display_name'].lower()} in {period.replace('_', ' ')} must match the data of Statistics summary table"
                    
                    key = f"{period}_{device['name']}"
                    data_referrers = cache["referrers"][key]
                    data_statistics = cache["statistics"][period]
                    
                    new_signups_fdm = str(data_statistics["new_signups_month"]).split('/')
                    statistics_signups = self.parse_int(new_signups_fdm[0])
                    statistics_fdm = self.parse_int(new_signups_fdm[1]) if len(new_signups_fdm) > 1 else 0
                    
                    pc_tracking = self.parse_fraction(data_statistics["tracking_pc_month"])
                    mobile_tracking = self.parse_fraction(data_statistics["tracking_mobile_month"])
                    
                    if device["name"] == "All":
                        statistics_total_clicks = pc_tracking["total"] + mobile_tracking["total"]
                        statistics_unique_clicks = pc_tracking["unique"] + mobile_tracking["unique"]
                    elif device["name"] == "Mobile":
                        statistics_total_clicks = mobile_tracking["total"]
                        statistics_unique_clicks = mobile_tracking["unique"]
                    else:
                        statistics_total_clicks = pc_tracking["total"]
                        statistics_unique_clicks = pc_tracking["unique"]
                    
                    referrers_total_clicks = 0
                    referrers_unique_clicks = 0
                    referrers_signups = 0
                    referrers_fdm = 0
                    
                    if data_referrers.get("has_data", True):
                        for site_data in data_referrers["site_urls_data"]:
                            referrers_total_clicks += self.parse_int(site_data["total_click"])
                            referrers_unique_clicks += self.parse_int(site_data["unique_click"])
                            referrers_signups += self.parse_int(site_data["signups"])
                            referrers_fdm += self.parse_int(site_data["fdm"])
                    
                    mismatches = []
                    click_type = "Total Clicks"
                    if device["name"] == "Mobile":
                        click_type = "Mobile Total Clicks"
                    elif device["name"] == "PC / Laptop":
                        click_type = "Desktop Total Clicks"
                    
                    if referrers_total_clicks != statistics_total_clicks:
                        mismatches.append(f"{click_type} mismatch: Statistics={statistics_total_clicks}, Referrers={referrers_total_clicks}")
                    
                    if referrers_signups != statistics_signups:
                        mismatches.append(f"Signups mismatch: Statistics={statistics_signups}, Referrers={referrers_signups}")
                    
                    if referrers_fdm != statistics_fdm:
                        mismatches.append(f"FDM mismatch: Statistics={statistics_fdm}, Referrers={referrers_fdm}")
                    
                    if mismatches:
                        raise Exception("\n".join(mismatches))
                    
                    results = {
                        "username": username,
                        "device_type": device["name"],
                        "from_date": cache[period]["date_range"]["from_date"],
                        "to_date": cache[period]["date_range"]["to_date"],
                        "statistics_total_clicks": statistics_total_clicks,
                        "statistics_unique_clicks": statistics_unique_clicks,
                        "referrers_total_clicks": referrers_total_clicks,
                        "referrers_unique_clicks": referrers_unique_clicks,
                        "statistics_signups": statistics_signups,
                        "referrers_signups": referrers_signups,
                        "statistics_fdm": statistics_fdm,
                        "referrers_fdm": referrers_fdm,
                        "click_type": click_type
                    }
                    
                    subAutoTestCase += self._format_test_results(results, device["display_name"])
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][0],
                sheet_name=Checklist_Sheet_Name
            )
            indexChl += 1
            
            subAutoTestCase = ''
            periods = ["last_month", "last_week", "current_month"]
            device_types = ["All", "PC / Laptop", "Mobile"]
            
            for period in periods:
                for device_type in device_types:
                    device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                    period_display = period.replace("_", " ")
                    
                    if subAutoTestCase:
                        subAutoTestCase += '\n\n'
                        
                    subAutoTestCase += f"- Verify that Total Clicks for Referrers {period_display} {'' if device_type == 'All' else 'by ' + device_display} are equal to Total Clicks for Landing Pages."
                    
                    key = f"{period}_{device_type}"
                    data_referrers = cache["referrers"][key]
                    data_landing_pages = cache["landing_pages"][key]
                    
                    referrers_total_clicks = 0
                    if data_referrers.get("has_data", True):
                        for site_data in data_referrers["site_urls_data"]:
                            referrers_total_clicks += self.parse_int(site_data["total_click"])
                    
                    landing_pages_total_clicks = 0
                    if data_landing_pages.get("has_data", True):
                        for page in data_landing_pages["pages_data"]:
                            landing_pages_total_clicks += self.parse_int(page["total_click"])
                    
                    has_data = data_referrers.get("has_data", True) and data_landing_pages.get("has_data", True)
                    
                    if has_data:
                        subAutoTestCase += f"\n     + Username: {username}"
                        subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                        subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                        
                        if referrers_total_clicks == landing_pages_total_clicks:
                            subAutoTestCase += f"\n     + Total Clicks match: {referrers_total_clicks}"
                        else:
                            subAutoTestCase += f"\n     + Total Clicks mismatch: Referrers={referrers_total_clicks}, Landing Pages={landing_pages_total_clicks}"
                    else:
                        subAutoTestCase += f"\n     + No data found for Total Clicks for Referrers or Landing Pages."
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][0],
                sheet_name=Checklist_Sheet_Name
            )
            indexChl += 1
            
            subAutoTestCase = ''
            
            for period in periods:
                for device_type in device_types:
                    device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                    period_display = period.replace("_", " ")
                    
                    if subAutoTestCase:
                        subAutoTestCase += '\n\n'
                        
                    subAutoTestCase += f"- Verify that Total Clicks for Referrers {period_display} {'' if device_type == 'All' else 'by ' + device_display} are equal to Total Clicks for Marketing Pages."
                    
                    key = f"{period}_{device_type}"
                    data_referrers = cache["referrers"][key]
                    data_marketing_pages = cache["marketing_pages"][key]
                    
                    referrers_total_clicks = 0
                    if data_referrers.get("has_data", True):
                        for site_data in data_referrers["site_urls_data"]:
                            referrers_total_clicks += self.parse_int(site_data["total_click"])
                    
                    marketing_pages_total_clicks = 0
                    if data_marketing_pages.get("has_data", True):
                        for channel in data_marketing_pages["channels_data"]:
                            marketing_pages_total_clicks += self.parse_int(channel["total_click"])
                    
                    has_data = data_referrers.get("has_data", True) and data_marketing_pages.get("has_data", True)
                    
                    if has_data:
                        subAutoTestCase += f"\n     + Username: {username}"
                        subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                        subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                        
                        if referrers_total_clicks == marketing_pages_total_clicks:
                            subAutoTestCase += f"\n     + Total Clicks match: {referrers_total_clicks}"
                        else:
                            subAutoTestCase += f"\n     + Total Clicks mismatch: Referrers={referrers_total_clicks}, Marketing Pages={marketing_pages_total_clicks}"
                    else:
                        subAutoTestCase += f"\n     + No data found for Total Clicks for Referrers or Marketing Pages."
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][0],
                sheet_name=Checklist_Sheet_Name
            )
            
        except Exception as e:
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][1],
                sheet_name=Checklist_Sheet_Name
            )
            indexChl += 1
            if indexChl < len(mainChecklist):
                for i in range(indexChl, len(mainChecklist)):
                    if i >= len(mainChecklist):
                        break
                    self.utils.update_result_to_ggsheet(
                        Data["TestCase_spread_sheet_id"], 
                        mainChecklist[i], 
                        testcase, 
                        "", 
                        Data["TestCase_Auto_Status"][2],
                        sheet_name=Checklist_Sheet_Name
                    )
            self.utils.page.extract_TestCaseFailed(e)

    def check_data_signups_and_fdm(self, testcase):

        cache, username = self.preload_all_data()
        
        mainChecklist = [
            "Verify that the Signups for Referrers equal the Signups for Landing Pages.",
            "Verify that the Signups for Referrers equal the Signups for Marketing Pages.",
            "Verify that the FDM for Referrers equal the FDM for Landing Pages.",
            "Verify that the FDM for Referrers equal the FDM for Marketing Pages."
        ]
        
        try:
            for checklist_index, comparison_type in enumerate([
                {"data_type": "signups", "compare_with": "landing_pages"},
                {"data_type": "signups", "compare_with": "marketing_pages"},
                {"data_type": "fdm", "compare_with": "landing_pages"},
                {"data_type": "fdm", "compare_with": "marketing_pages"}
            ]):
                data_type = comparison_type["data_type"]
                compare_with = comparison_type["compare_with"]
                
                data_type_display = data_type.capitalize()
                compare_with_display = "Landing Pages" if compare_with == "landing_pages" else "Marketing Pages"
                
                subAutoTestCase = ''
                periods = ["last_month", "last_week", "current_month"]
                device_types = ["All", "PC / Laptop", "Mobile"]
                
                for period in periods:
                    for device_type in device_types:
                        device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                        period_display = period.replace("_", " ")
                        
                        if subAutoTestCase:
                            subAutoTestCase += '\n\n'
                            
                        subAutoTestCase += f"- Verify that {data_type_display} for Referrers {period_display} {'' if device_type == 'All' else 'by ' + device_display} are equal to {data_type_display} for {compare_with_display}."
                        
                        key = f"{period}_{device_type}"
                        data_referrers = cache["referrers"][key]
                        data_pages = cache[compare_with][key]
                        
                        referrers_value = 0
                        if data_referrers.get("has_data", True):
                            for site_data in data_referrers["site_urls_data"]:
                                referrers_value += self.parse_int(site_data[data_type])
                        
                        pages_value = 0
                        if data_pages.get("has_data", True):
                            if compare_with == "landing_pages":
                                for page in data_pages["pages_data"]:
                                    pages_value += self.parse_int(page[data_type])
                            else:
                                for channel in data_pages["channels_data"]:
                                    pages_value += self.parse_int(channel[data_type])
                        
                        has_data = data_referrers.get("has_data", True) and data_pages.get("has_data", True)
                        
                        if has_data:
                            subAutoTestCase += f"\n     + Username: {username}"
                            subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                            subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                            
                            if referrers_value == pages_value:
                                subAutoTestCase += f"\n     + {data_type_display} match: {referrers_value}"
                            else:
                                subAutoTestCase += f"\n     + {data_type_display} mismatch: Referrers={referrers_value}, {compare_with_display}={pages_value}"
                        else:
                            subAutoTestCase += f"\n     + No data found for {data_type_display} for Referrers or {compare_with_display}."
                
                self.utils.update_result_to_ggsheet(
                    Data["TestCase_spread_sheet_id"], 
                    mainChecklist[checklist_index], 
                    testcase, 
                    subAutoTestCase, 
                    Data["TestCase_Auto_Status"][0],
                    sheet_name=Checklist_Sheet_Name
                )
                
        except Exception as e:
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[checklist_index], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][1],
                sheet_name=Checklist_Sheet_Name
            )
            checklist_index += 1
            if checklist_index < len(mainChecklist):
                for i in range(checklist_index, len(mainChecklist)):
                    if i >= len(mainChecklist):
                        break
                    self.utils.update_result_to_ggsheet(
                        Data["TestCase_spread_sheet_id"], 
                        mainChecklist[i], 
                        testcase, 
                        "", 
                        Data["TestCase_Auto_Status"][2],
                        sheet_name=Checklist_Sheet_Name
                    )
            self.utils.page.extract_TestCaseFailed(e)