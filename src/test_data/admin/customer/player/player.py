PLAYER_API = "/Portal/Player/GetMemberList"

PLAYER_HEADERS = {
    "content-type": "application/json;charset=UTF-8",
    "accept": "application/json, text/plain, */*"
}

PLAYER_REQUEST_TEMPLATE = {
    "AffName": "",
    "UserName": "",
    "IbcUserName": "",
    "IsIncludeRemovedPlayer": False,
    "PageIndex": 1,
    "PageSize": 20
} 