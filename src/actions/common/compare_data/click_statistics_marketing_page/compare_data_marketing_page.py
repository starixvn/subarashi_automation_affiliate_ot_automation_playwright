from config.constants.settings import *
env = ENVIRONMENT
import random
from datetime import datetime, timedelta

from src.actions.common.get_data_on_function.get_data_customer import GetDataCustomer
from src.test_data.common.data_common import *
from src.actions.common.get_data_on_function.get_data_player import GetDataPlayer

from src.test_data.common.data_click_statistics.data_marketing_pages.data_marketing_pages_last_month import DataMarketingPagesLastMonth
from src.test_data.common.data_click_statistics.data_marketing_pages.data_marketing_pages_last_week import DataMarketingPagesLastWeek
from src.test_data.common.data_click_statistics.data_marketing_pages.data_marketing_pages_yesterday import DataMarketingPagesYesterday

Data = {
    "TestCase_spread_sheet_id": TestCase_Spread_Sheet_Id,
    "TestCase_Auto_Status": TestCase_Auto_Status,
    "Marketing_Pages_Last_Month": DataMarketingPagesLastMonth.data_marketing_pages_last_month,
    "Marketing_Pages_Last_Week": DataMarketingPagesLastWeek.data_marketing_pages_last_week,
    "Marketing_Pages_Yesterday": DataMarketingPagesYesterday.data_marketing_pages_yesterday,
}
Checklist_Sheet_Name = "Compare_Data_Clickstatistics"

class CompareDataMarketingPage(GetDataCustomer):
    def __init__(self):
        super().__init__()
        self.get_data_customer = GetDataCustomer()

    def _compare_channels_data(self, baseline_channels_data, current_channels_data):
        if len(baseline_channels_data) != len(current_channels_data):
            raise Exception(f"Number of channels mismatch. Baseline: {len(baseline_channels_data)}, Current: {len(current_channels_data)}")
        
        for baseline_channel_data in baseline_channels_data:
            channel_name = baseline_channel_data["channel_name"]
            language = baseline_channel_data["language"]
            channel_found = False
            
            for current_channel in current_channels_data:
                if current_channel["channel_name"].lower() == channel_name.lower() and current_channel["language"].lower() == language.lower():
                    channel_found = True
                    if int(current_channel["total_click"]) != baseline_channel_data["total_click"]:
                        raise Exception(f"Total clicks mismatch for channel {channel_name} - {language}. Baseline: {baseline_channel_data['total_click']}, Current: {current_channel['total_click']}")
                    if int(current_channel["unique_click"]) != baseline_channel_data["unique_click"]:
                        raise Exception(f"Unique clicks mismatch for channel {channel_name} - {language}. Baseline: {baseline_channel_data['unique_click']}, Current: {current_channel['unique_click']}")
                    if int(current_channel["signups"]) != baseline_channel_data["signups"]:
                        raise Exception(f"Signups mismatch for channel {channel_name} - {language}. Baseline: {baseline_channel_data['signups']}, Current: {current_channel['signups']}")
                    if int(current_channel["fdm"]) != baseline_channel_data["fdm"]:
                        raise Exception(f"FDM mismatch for channel {channel_name} - {language}. Baseline: {baseline_channel_data['fdm']}, Current: {current_channel['fdm']}")
                    break
            
            if not channel_found and channel_name.lower() != "none" and channel_name.strip() != "":
                raise Exception(f"Channel '{channel_name} - {language}' not found in current data")
    
    def _compare_channel_details(self, baseline_channel_details_data, current_channel_details_data):
        for channel_key, baseline_urls in baseline_channel_details_data.items():
            if "none" in channel_key.lower():
                continue
            
            if channel_key not in current_channel_details_data:
                raise Exception(f"Channel details for '{channel_key}' not found in current data")
            
            current_urls = current_channel_details_data[channel_key]
            
            if len(baseline_urls) != len(current_urls):
                raise Exception(f"Number of URLs mismatch for channel {channel_key}. Baseline: {len(baseline_urls)}, Current: {len(current_urls)}")
            
            for baseline_url in baseline_urls:
                url_found = False
                for current_url in current_urls:
                    if current_url["url"] == baseline_url["url"]:
                        url_found = True
                        if int(current_url["total_clicks"]) != baseline_url["total_clicks"]:
                            raise Exception(f"Total clicks mismatch for URL {baseline_url['url']}. Baseline: {baseline_url['total_clicks']}, Current: {current_url['total_clicks']}")
                        if int(current_url["unique_clicks"]) != baseline_url["unique_clicks"]:
                            raise Exception(f"Unique clicks mismatch for URL {baseline_url['url']}. Baseline: {baseline_url['unique_clicks']}, Current: {current_url['unique_clicks']}")
                        if int(current_url["signups"]) != baseline_url["signups"]:
                            raise Exception(f"Signups mismatch for URL {baseline_url['url']}. Baseline: {baseline_url['signups']}, Current: {current_url['signups']}")
                        if int(current_url["fdm"]) != baseline_url["fdm"]:
                            raise Exception(f"FDM mismatch for URL {baseline_url['url']}. Baseline: {baseline_url['fdm']}, Current: {current_url['fdm']}")
                        break
                
                if not url_found and baseline_url["url"].lower() != "none" and baseline_url["url"].strip() != "":
                    raise Exception(f"URL '{baseline_url['url']}' not found in current data for channel {channel_key}")
    
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
        elif period == "last_week":
            to_date = (today - timedelta(days=today.weekday() + 1)).strftime("%m-%d-%Y")  # Last Sunday
            from_date = (today - timedelta(days=today.weekday() + 7)).strftime("%m-%d-%Y")  # Previous Monday
            month_date = today.strftime("%m-%Y")
        elif period == "yesterday":
            yesterday = today - timedelta(days=1)
            from_date = yesterday.strftime("%m-%d-%Y")
            to_date = yesterday.strftime("%m-%d-%Y")
            month_date = yesterday.strftime("%m-%Y")
        else:  # current_month
            first_day_current_month = today.replace(day=1)
            from_date = first_day_current_month.strftime("%m-%d-%Y")
            to_date = today.strftime("%m-%d-%Y")
            month_date = today.strftime("%m-%Y")
        
        return {
            "from_date": from_date,
            "to_date": to_date,
            "month_date": month_date
        }

    def preload_all_data(self):
        periods = ["last_month", "last_week", "current_month"]
        stats_periods = ["last_month", "current_month"]
        
        cache = {
            "marketing_pages": {},
            "referrers": {},
            "landing_pages": {},
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
            
            if period in stats_periods:
                cache["statistics"][period] = self.get_data_statistics_in_customer(
                    username, date_range["month_date"]
                )
            
            data_marketing_pages = self.get_data_marketing_pages_in_customer(
                username, "All", date_range["from_date"], date_range["to_date"], get_detail=True
            )
            cache["marketing_pages"][period] = data_marketing_pages
            
            data_referrers = self.get_data_referrers_in_customer(
                username, date_range["from_date"], date_range["to_date"], "All", get_detail=False
            )
            cache["referrers"][period] = data_referrers
            
            data_landing_pages = self.get_data_landing_pages_in_customer(
                username, "All", "All", date_range["from_date"], date_range["to_date"], "All", get_detail=False
            )
            cache["landing_pages"][period] = data_landing_pages
        
        print("All data preloaded successfully!")
        return cache, username

    def check_data_marketing_pages_filter_by_date_language(self, testcase):
        subAutoTestCase = ''
        mainChecklist = [
            "Verify that the Marketing Page data displays correctly according to the date picker.",
            "Verify that the Marketing Page data displays correctly according to the Language filter."
        ]
        indexChl = 0
        try:
            if "Marketing_Pages_Last_Month" not in Data or not Data["Marketing_Pages_Last_Month"]:
                raise Exception("Baseline data not found. Please run the job to collect baseline data first.")
                
            subAutoTestCase = '- Verify that the data displayed is correct according to the date picker'
            
            date_ranges = {
                "Last Month": Data["Marketing_Pages_Last_Month"],
                "Last Week": Data["Marketing_Pages_Last_Week"],
                "Yesterday": Data["Marketing_Pages_Yesterday"]
            }
            
            for period_name, baseline_data in date_ranges.items():
                username = baseline_data["metadata"]["filters"]["username"]
                language = baseline_data["metadata"]["filters"]["language"]
                from_date = baseline_data["metadata"]["period"]["from_date"]
                to_date = baseline_data["metadata"]["period"]["to_date"]
                include_inactive = baseline_data["metadata"]["filters"].get("include_inactive_tracking", False)
                
                current_data = self.get_data_marketing_pages_in_customer(username, language, from_date, to_date, include_inactive)
                
                baseline_has_data = baseline_data["metadata"].get("has_data", True)
                current_has_data = current_data.get("has_data", True)
                
                if not baseline_has_data and not current_has_data:
                    subAutoTestCase += f"\n     + {period_name}: No data expected - verified no data is present"
                elif not baseline_has_data and current_has_data:
                    raise Exception(f"{period_name}: Baseline data has no results but current query returned data. This suggests a data inconsistency.")
                elif baseline_has_data and not current_has_data:
                    raise Exception(f"{period_name}: No current data found for user {username} from {from_date} to {to_date} with language {language}, but baseline data exists")
                else:
                    self._compare_channels_data(baseline_data["channels_data"], current_data["channels_data"])
                    self._compare_channel_details(baseline_data["channel_details_data"], current_data["channel_details_data"])
                    subAutoTestCase += f"\n     + {period_name}: Successfully verified data with date range {from_date} to {to_date}"
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            indexChl += 1
            subAutoTestCase = ''
            
            subAutoTestCase = '- Verify that the data displayed is correct according to the Language filter'
            
            baseline_data = Data["Marketing_Pages_Last_Month"]
            username = baseline_data["metadata"]["filters"]["username"]
            from_date = baseline_data["metadata"]["period"]["from_date"]
            to_date = baseline_data["metadata"]["period"]["to_date"]
            include_inactive = baseline_data["metadata"]["filters"].get("include_inactive_tracking", False)
            
            languages = set()
            for channel_data in baseline_data["channels_data"]:
                if channel_data["language"] and channel_data["language"].lower() != "none" and channel_data["language"].strip() != "":
                    languages.add(channel_data["language"])
            
            if languages:
                language = next(iter(languages))
                current_data = self.get_data_marketing_pages_in_customer(username, language, from_date, to_date, include_inactive)
                
                if current_data.get("has_data", True):
                    for channel_data in current_data["channels_data"]:
                        if channel_data["language"].lower() != language.lower():
                            raise Exception(f"Language filter did not work correctly. Found language {channel_data['language']} when filtering for {language}")
                    
                    subAutoTestCase += f"\n     + Successfully verified Language filter for '{language}'"
                else:
                    subAutoTestCase += f"\n     + No data found when filtering for language '{language}'"
            else:
                subAutoTestCase += "\n     + No valid language found in baseline data to test the filter"
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            
        except Exception as e:
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][1], sheet_name=Checklist_Sheet_Name)
            indexChl += 1
            if indexChl < len(mainChecklist):
                for i in range(indexChl, len(mainChecklist)):
                    if i >= len(mainChecklist):
                        break
                    self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[i], testcase, "", Data["TestCase_Auto_Status"][2], sheet_name=Checklist_Sheet_Name)
            self.utils.page.extract_TestCaseFailed(e)

    def check_data_marketing_pages_collapsed_expanded_match(self, testcase):
        mainChecklist = ["Verify that the sum of the collapsed data equals the data in the expanded section."]
        indexChl = 0
        
        try:
            subAutoTestCase = '- Verify that the sum of the collapsed data equals the data in the expanded section'
            
            username = self._get_username()
            periods = ["last_month", "last_week", "current_month"]
            
            for period in periods:
                date_range = self._get_date_range(period)
                period_display = period.replace("_", " ")
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify for {period_display} that channel totals match the sum of their detail URLs"
                
                data_marketing_pages = self.get_data_marketing_pages_in_customer(
                    username, "All", date_range["from_date"], date_range["to_date"], get_detail=True
                )
                
                if not data_marketing_pages.get("has_data", True):
                    subAutoTestCase += f"\n     + No data found for Marketing Pages in {period_display}."
                    continue
                
                subAutoTestCase += f"\n     + Username: {username}"
                subAutoTestCase += f"\n     + From Date: {date_range['from_date']}"
                subAutoTestCase += f"\n     + To Date: {date_range['to_date']}"
                
                mismatches = []
                
                for channel_data in data_marketing_pages["channels_data"]:
                    channel_name = channel_data["channel_name"]
                    language = channel_data["language"]
                    channel_key = f"{channel_name} - {language}"
                    
                    if channel_key not in data_marketing_pages["channel_details_data"]:
                        continue
                    
                    channel_details = data_marketing_pages["channel_details_data"][channel_key]
                    
                    detail_total_clicks = 0
                    detail_unique_clicks = 0
                    detail_signups = 0
                    detail_fdm = 0
                    
                    for url_data in channel_details:
                        detail_total_clicks += self.parse_int(url_data["total_clicks"])
                        detail_unique_clicks += self.parse_int(url_data["unique_clicks"])
                        detail_signups += self.parse_int(url_data["signups"])
                        detail_fdm += self.parse_int(url_data["fdm"])
                    
                    channel_total_click = self.parse_int(channel_data["total_click"])
                    channel_unique_click = self.parse_int(channel_data["unique_click"])
                    channel_signups = self.parse_int(channel_data["signups"])
                    channel_fdm = self.parse_int(channel_data["fdm"])
                    
                    if detail_total_clicks != channel_total_click:
                        mismatches.append(f"Total clicks mismatch for channel '{channel_key}': Channel={channel_total_click}, Sum of details={detail_total_clicks}")
                    
                    if detail_unique_clicks != channel_unique_click:
                        mismatches.append(f"Unique clicks mismatch for channel '{channel_key}': Channel={channel_unique_click}, Sum of details={detail_unique_clicks}")
                    
                    if detail_signups != channel_signups:
                        mismatches.append(f"Signups mismatch for channel '{channel_key}': Channel={channel_signups}, Sum of details={detail_signups}")
                    
                    if detail_fdm != channel_fdm:
                        mismatches.append(f"FDM mismatch for channel '{channel_key}': Channel={channel_fdm}, Sum of details={detail_fdm}")
                
                if mismatches:
                    subAutoTestCase += f"\n     + Failed: {len(mismatches)} mismatches found:"
                    for mismatch in mismatches[:3]:  # Show first 3 mismatches to avoid too large report
                        subAutoTestCase += f"\n       - {mismatch}"
                    if len(mismatches) > 3:
                        subAutoTestCase += f"\n       - ... and {len(mismatches) - 3} more"
                else:
                    subAutoTestCase += f"\n     + Verified: All channel totals match the sum of their detail URLs."
            
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
            self.utils.page.extract_TestCaseFailed(e)

    def check_data_marketing_pages_click_statistics_compare(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = [
            "Verify that the Total Clicks on the Marketing Page equal the Total Clicks of Referrers.",
            "Verify that the Total Clicks on the Marketing Page equal the Total Clicks of Landing Pages."
        ]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            periods = ["last_month", "last_week", "current_month"]
            
            for period in periods:
                period_display = period.replace("_", " ")
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                    
                subAutoTestCase += f"- Verify that Total Clicks for Marketing Pages {period_display} are equal to Total Clicks for Referrers."
                
                data_marketing_pages = cache["marketing_pages"][period]
                data_referrers = cache["referrers"][period]
                
                marketing_pages_total_clicks = 0
                if data_marketing_pages.get("has_data", True):
                    for channel in data_marketing_pages["channels_data"]:
                        marketing_pages_total_clicks += self.parse_int(channel["total_click"])
                
                referrers_total_clicks = 0
                if data_referrers.get("has_data", True):
                    for site_data in data_referrers["site_urls_data"]:
                        referrers_total_clicks += self.parse_int(site_data["total_click"])
                
                has_data = data_marketing_pages.get("has_data", True) and data_referrers.get("has_data", True)
                
                if has_data:
                    subAutoTestCase += f"\n     + Username: {username}"
                    subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                    subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                    
                    if marketing_pages_total_clicks == referrers_total_clicks:
                        subAutoTestCase += f"\n     + Total Clicks match: {marketing_pages_total_clicks}"
                    else:
                        subAutoTestCase += f"\n     + Total Clicks mismatch: Marketing Pages={marketing_pages_total_clicks}, Referrers={referrers_total_clicks}"
                else:
                    subAutoTestCase += f"\n     + No data found for Total Clicks for Marketing Pages or Referrers."
            
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
                period_display = period.replace("_", " ")
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                    
                subAutoTestCase += f"- Verify that Total Clicks for Marketing Pages {period_display} are equal to Total Clicks for Landing Pages."
                
                data_marketing_pages = cache["marketing_pages"][period]
                data_landing_pages = cache["landing_pages"][period]
                
                marketing_pages_total_clicks = 0
                if data_marketing_pages.get("has_data", True):
                    for channel in data_marketing_pages["channels_data"]:
                        marketing_pages_total_clicks += self.parse_int(channel["total_click"])
                
                landing_pages_total_clicks = 0
                if data_landing_pages.get("has_data", True):
                    for page_data in data_landing_pages["pages_data"]:
                        landing_pages_total_clicks += self.parse_int(page_data["total_click"])
                
                has_data = data_marketing_pages.get("has_data", True) and data_landing_pages.get("has_data", True)
                
                if has_data:
                    subAutoTestCase += f"\n     + Username: {username}"
                    subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                    subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                    
                    if marketing_pages_total_clicks == landing_pages_total_clicks:
                        subAutoTestCase += f"\n     + Total Clicks match: {marketing_pages_total_clicks}"
                    else:
                        subAutoTestCase += f"\n     + Total Clicks mismatch: Marketing Pages={marketing_pages_total_clicks}, Landing Pages={landing_pages_total_clicks}"
                else:
                    subAutoTestCase += f"\n     + No data found for Total Clicks for Marketing Pages or Landing Pages."
            
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
            "Verify that the Signups on the Marketing Page equal the Total Clicks of Referrers.",
            "Verify that the Signups on the Marketing Page equal the Total Clicks of Landing Pages.",
            "Verify that the FDM on the Marketing Page equals the Total Clicks of Referrers.",
            "Verify that the FDM on the Marketing Page equals the Total Clicks of Landing Pages."
        ]
        
        try:
            for checklist_index, comparison_type in enumerate([
                {"data_type": "signups", "compare_with": "referrers"},
                {"data_type": "signups", "compare_with": "landing_pages"},
                {"data_type": "fdm", "compare_with": "referrers"},
                {"data_type": "fdm", "compare_with": "landing_pages"}
            ]):
                data_type = comparison_type["data_type"]
                compare_with = comparison_type["compare_with"]
                
                data_type_display = data_type.capitalize()
                compare_with_display = "Referrers" if compare_with == "referrers" else "Landing Pages"
                
                subAutoTestCase = ''
                periods = ["last_month", "last_week", "current_month"]
                
                for period in periods:
                    period_display = period.replace("_", " ")
                    
                    if subAutoTestCase:
                        subAutoTestCase += '\n\n'
                        
                    subAutoTestCase += f"- Verify that {data_type_display} for Marketing Pages {period_display} are equal to {data_type_display} for {compare_with_display}."
                    
                    data_marketing_pages = cache["marketing_pages"][period]
                    data_compare = cache[compare_with][period]
                    
                    marketing_pages_value = 0
                    if data_marketing_pages.get("has_data", True):
                        for channel in data_marketing_pages["channels_data"]:
                            marketing_pages_value += self.parse_int(channel[data_type])
                    
                    compare_value = 0
                    if data_compare.get("has_data", True):
                        if compare_with == "referrers":
                            for site_data in data_compare["site_urls_data"]:
                                compare_value += self.parse_int(site_data[data_type])
                        else:  # landing_pages
                            for page_data in data_compare["pages_data"]:
                                compare_value += self.parse_int(page_data[data_type])
                    
                    has_data = data_marketing_pages.get("has_data", True) and data_compare.get("has_data", True)
                    
                    if has_data:
                        subAutoTestCase += f"\n     + Username: {username}"
                        subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                        subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                        
                        if marketing_pages_value == compare_value:
                            subAutoTestCase += f"\n     + {data_type_display} match: {marketing_pages_value}"
                        else:
                            subAutoTestCase += f"\n     + {data_type_display} mismatch: Marketing Pages={marketing_pages_value}, {compare_with_display}={compare_value}"
                    else:
                        subAutoTestCase += f"\n     + No data found for {data_type_display} for Marketing Pages or {compare_with_display}."
                
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

    def verify_signups_fdm_statistics_match(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = [
            "Verify that the total Signups for the month equal the total Signups in the Statistics data table.",
            "Verify that the total FDM for the month equals the total Signups in the Statistics data table."
        ]
        
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            time_periods = ["last_month", "current_month"]
            
            for period in time_periods:
                period_display = period.replace("_", " ")
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify that total Signups for Marketing Pages in {period_display} match the Statistics data table"
                
                data_statistics = cache["statistics"][period]
                data_marketing_pages = cache["marketing_pages"][period]
                
                marketing_pages_signups = 0
                if data_marketing_pages.get("has_data", True):
                    for channel in data_marketing_pages["channels_data"]:
                        marketing_pages_signups += self.parse_int(channel["signups"])
                
                new_signups_fdm = str(data_statistics["new_signups_month"]).split('/')
                statistics_signups = self.parse_int(new_signups_fdm[0])
                
                subAutoTestCase += f"\n     + Username: {username}"
                subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                
                if marketing_pages_signups == statistics_signups:
                    subAutoTestCase += f"\n     + Signups match: Statistics={statistics_signups}, Marketing Pages={marketing_pages_signups}"
                else:
                    subAutoTestCase += f"\n     + Signups mismatch: Statistics={statistics_signups}, Marketing Pages={marketing_pages_signups}"
            
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
            
            for period in time_periods:
                period_display = period.replace("_", " ")
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify that total FDM for Marketing Pages in {period_display} match the Statistics data table"
                
                data_statistics = cache["statistics"][period]
                data_marketing_pages = cache["marketing_pages"][period]
                
                marketing_pages_fdm = 0
                if data_marketing_pages.get("has_data", True):
                    for channel in data_marketing_pages["channels_data"]:
                        marketing_pages_fdm += self.parse_int(channel["fdm"])
                
                new_signups_fdm = str(data_statistics["new_signups_month"]).split('/')
                statistics_fdm = self.parse_int(new_signups_fdm[1]) if len(new_signups_fdm) > 1 else 0
                
                subAutoTestCase += f"\n     + Username: {username}"
                subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                
                if marketing_pages_fdm == statistics_fdm:
                    subAutoTestCase += f"\n     + FDM match: Statistics={statistics_fdm}, Marketing Pages={marketing_pages_fdm}"
                else:
                    subAutoTestCase += f"\n     + FDM mismatch: Statistics={statistics_fdm}, Marketing Pages={marketing_pages_fdm}"
            
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

    def verify_total_clicks_has_unique_clicks(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = [
            "Verify that if there is data in the Total Clicks column, the Unique Click column also contains data."
        ]
        
        indexChl = 0
        subAutoTestCase = ''
        
        try:
            periods = ["last_month", "last_week", "current_month"]
            
            for period in periods:
                period_display = period.replace("_", " ")
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify that for Marketing Pages {period_display}, if Total Clicks has data, then Unique Clicks also has data"
                
                data_marketing_pages = cache["marketing_pages"][period]
                
                subAutoTestCase += f"\n     + Username: {username}"
                subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                
                if not data_marketing_pages.get("has_data", True):
                    subAutoTestCase += f"\n     + No data found for Marketing Pages."
                    continue
                
                violations = []
                total_channels = 0
                channels_with_total_clicks = 0
                
                for channel_data in data_marketing_pages["channels_data"]:
                    channel_name = channel_data["channel_name"]
                    language = channel_data["language"]
                    channel_key = f"{channel_name} - {language}"
                    total_clicks = self.parse_int(channel_data["total_click"])
                    unique_clicks = self.parse_int(channel_data["unique_click"])
                    
                    total_channels += 1
                    
                    if total_clicks > 0:
                        channels_with_total_clicks += 1
                        if unique_clicks == 0:
                            violations.append(f"Channel '{channel_key}' has Total Clicks ({total_clicks}) but no Unique Clicks")
                
                for channel_key, url_details in data_marketing_pages["channel_details_data"].items():
                    for url_data in url_details:
                        url = url_data["url"]
                        total_clicks = self.parse_int(url_data["total_clicks"])
                        unique_clicks = self.parse_int(url_data["unique_clicks"])
                        
                        if total_clicks > 0 and unique_clicks == 0:
                            violations.append(f"URL '{url}' under Channel '{channel_key}' has Total Clicks ({total_clicks}) but no Unique Clicks")
                
                if not channels_with_total_clicks:
                    subAutoTestCase += f"\n     + No channels with Total Clicks data found."
                elif violations:
                    subAutoTestCase += f"\n     + Failed: {len(violations)} channels/URLs have Total Clicks but no Unique Clicks:"
                    for violation in violations[:3]:  # Show first 3 violations to avoid too large report
                        subAutoTestCase += f"\n       - {violation}"
                    if len(violations) > 3:
                        subAutoTestCase += f"\n       - ... and {len(violations) - 3} more"
                else:
                    subAutoTestCase += f"\n     + Verified: All {channels_with_total_clicks} channels/URLs with Total Clicks also have Unique Clicks data."
            
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
            self.utils.page.extract_TestCaseFailed(e)