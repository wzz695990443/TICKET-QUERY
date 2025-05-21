import requests
from pydantic import BaseModel
import loginSSO
import config

class queryTicketList_body(BaseModel):
    goodsName: str = ""
    goodsCode: str = ""
    ticketType: str = "GENERAL,RANG,QUARTER,TIMES,SPEC,SESSION,LINK"
    beginResrvDate: str = ""
    endResrvDate: str = ""
    beginDate: str = ""
    endDate: str = ""
    hotelGroupCode: str = ""
    hotelCode: str = "0"
    unitCode: str = ""
    firstResult: int = 0
    pageSize: int = 10
    
    

class queryTicketList:
    def __init__(self, token=None, body: queryTicketList_body|None = None):
        self.setting = config.get_settings()
        self.token = token or loginSSO.loginSSO_request()["retVal"]["jwtToken"]
        self.queryTicketList_url = f"https://{self.setting.TICKET_URL}/platform-ticket/bks/ticket/goods/queryTicketList"
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
            "authorization": self.token,
            "origin": f"https://{self.setting.TICKET_URL}",
            "priority": "u=1, i",
            "Content-Type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
            "Cookie": "",
        }
        self.body = {
            "goodsName": "",
            "goodsCode": "",
            "ticketType": "GENERAL,RANG,QUARTER,TIMES,SPEC,SESSION,LINK",
            "beginResrvDate": "",
            "endResrvDate": "",
            "beginDate": "",
            "endDate": "",
            "hotelGroupCode": self.setting.ORGCODE,
            "hotelCode": "0",
            "unitCode": "HMSD",
            "firstResult": 0,
            "pageSize": 10,
        }


def queryTicketList_request(pageSize: int):
    json = loginSSO.loginSSO_request()
    token = json["retVal"]["jwtToken"]
    url = (
        f"https://{config.ticket_url}/platform-ticket/bks/ticket/goods/queryTicketList"
    )
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
        "authorization": token,
        "origin": f"https://{config.ticket_url}",
        "priority": "u=1, i",
        "Content-Type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
        "Cookie": "",
    }
    body = {
        "goodsName": "",
        "goodsCode": "",
        "ticketType": "GENERAL,RANG,QUARTER,TIMES,SPEC,SESSION,LINK",
        "beginResrvDate": "",
        "endResrvDate": "",
        "beginDate": "",
        "endDate": "",
        "hotelGroupCode": "HMSD",
        "hotelCode": "0",
        "unitCode": "HMSD",
        "firstResult": 0,
        "pageSize": pageSize,
    }
    try:
        response = requests.post(url=url, headers=headers, verify=False, json=body)
        print("success queryTicketList")
        return response.json()
    except Exception as e:
        print("queryTicketList error:", e)
