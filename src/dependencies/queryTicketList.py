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
        self._setting = config.get_settings()
        self._token = token or loginSSO.loginSSO_request()["retVal"]["jwtToken"]
        self._url = f"https://{self._setting.TICKET_URL}/platform-ticket/bks/ticket/goods/queryTicketList"
        self._headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
            "authorization": self._token,
            "origin": f"https://{self._setting.TICKET_URL}",
            "priority": "u=1, i",
            "Content-Type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
            "Cookie": "",
        }
        self._body = body or {
            "goodsName": "",
            "goodsCode": "",
            "ticketType": "GENERAL,RANG,QUARTER,TIMES,SPEC,SESSION,LINK",
            "beginResrvDate": "",
            "endResrvDate": "",
            "beginDate": "",
            "endDate": "",
            "hotelGroupCode": self._setting.ORGCODE,
            "hotelCode": "0",
            "unitCode": self._setting.ORGCODE,
            "firstResult": 0,
            "pageSize": 10,
        }

    def request(self):
        try:
            response = requests.post(
                url=self._url,
                headers=self._headers,
                verify=False,
                json=self._body,
            )
            print("success loginSSO")
            return response.json()
        except Exception as e:
            print("loginSSO error:", e)

    @property
    def body(self):
        return self._body
    @body.setter
    def body(self, body: queryTicketList_body):
        self._body = body.model_dump()
