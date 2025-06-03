LANDING_PAGE_STATISTICS_API = "/Admin/Portal/UserPanel/LandingPageStatistics/GetLandingPageStatisticsList"

LANDING_PAGE_DETAILS_API = "/Admin/Portal/UserPanel/LandingPageStatistics/GetLandingPageStatisticsDetailList"

DEVICE_TYPE_MAPPING = {
    "All": -1,
    "PC / Laptop": 0,
    "Mobile": 1
}

REQUIRED_HEADERS = {
    "content-type": "application/json;charset=UTF-8",
    "accept": "application/json, text/plain, */*"
}

REQUEST_BODY_TEMPLATE = {
    "deviceType": -1,
    "fromDate": None,
    "toDate": None,
    "selectedPage": "",
    "languageCode": "",
    "affId": None
}

DETAILS_REQUEST_BODY_TEMPLATE = {
    "selectedPage": "",
    "languageCode": "",
    "fromDate": None,
    "toDate": None,
    "deviceType": -1,
    "affId": None,
    "pageIndex": 1,
    "pageSize": 100
} 