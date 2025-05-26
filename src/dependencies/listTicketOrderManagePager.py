import requests
from pydantic import BaseModel
import loginSSO
import config

class listTicketOrderManagePager_body(BaseModel):
    firstResult: int = 0
    pageSize: int = 10
    hotelGroupCode: str = ""
    unitCode: str = ""
    orderNo: str = ""
    mobile: str = ""
    gcRsvNo: str = ""
    otaRsvNo: str = ""
    paySta: str = ""
    payType: str = ""
    pickTicketSta: str = ""
    stationCode: str = ""
    salesmanCode: str = ""
    orderChannel: str = ""
    rsvHotelCode: str = ""
    companyCode: str = ""
    idNo: str = ""
    rsvType: str = "ALL"
    no: str = ""
    goodsCode: str = ""
    chipId: str = ""
    sta: str = "W,I,O,X,F,U"
    orderBeginDate: str = ""
    orderEndDate: str = ""
    beginDate: str = ""
    endDate: str = ""
    useBeginDatetime: str = ""
    useEndDatetime: str = ""

class listTicketOrderManagePager:
    def __init__(self, token=None, body: listTicketOrderManagePager_body|None = None):
        self._setting = config.get_settings()
        self._token = token or loginSSO.loginSSO_request()["retVal"]["jwtToken"]
        self._url = f"https://{self._setting.TICKET_URL}/platform-ticket/bks/ticket/order/listTicketOrderManagePager"
        self._headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
            "authorization": self._token,
            "origin": f"https://{self._setting.TICKET_URL}",
            "priority": "u=1, i",
            "Content-Type": "application/json",
            "Cookie": "",
        }
        self._body = body or {
            "firstResult": 0,
            "pageSize": 10,
            "hotelGroupCode": self._setting.ORGCODE,
            "unitCode": self._setting.ORGCODE,
            "orderNo": "",
            "mobile": "",
            "gcRsvNo": "",
            "otaRsvNo": "",
            "paySta": "",
            "payType": "",
            "pickTicketSta": "",
            "stationCode": "",
            "salesmanCode": "",
            "orderChannel": "",
            "rsvHotelCode": "",
            "companyCode": "",
            "idNo": "",
            "rsvType": "ALL",
            "no": "",
            "goodsCode": "",
            "chipId": "",
            "sta": "W,I,O,X,F,U",
            "orderBeginDate": "",
            "orderEndDate": "",
            "beginDate": "",
            "endDate": "",
            "useBeginDatetime": "",
            "useEndDatetime": "",
        }

    def request(self):
        try:
            if type(self._body) == listTicketOrderManagePager_body:
                self._body = self._body.model_dump()
            response = requests.post(
                url=self._url,
                headers=self._headers,
                verify=False,
                json=self._body,
            )
            print("success listTicketOrderManagePager")
            return response.json()
        except Exception as e:
            print("listTicketOrderManagePager error:", e)
            return None

    @property
    def body(self):
        return self._body
    @body.setter
    def body(self, body: listTicketOrderManagePager_body):
        self._body = body.model_dump()
