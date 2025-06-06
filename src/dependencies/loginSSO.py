import config
import requests


class loginSSO:
    def __init__(self):
        self._setting = config.get_settings()
        self._loginSSO_url = f"https://{self._setting.GC_URL}/uc-web/v2/password/loginSSO"
        self._loginSSO_headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
            "content-type": "application/json",
            "language": "zh-CN",
            "origin": f"https://{self._setting.GC_URL}",
            "priority": "u=1, i",
            "referer": f"https://{self._setting.GC_URL}/login?redirect=%2Fmain%2FPLATFORM_TICKET%2FreportFrPage",
            "repeat-login": "T",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
        }
        self._loginSSO_body = {
            "orgCode": self._setting.ORGCODE,
            "userCode": self._setting.USER_CODE,
            "password": self._setting.PASSWORD,
        }
    # 登录SSO,获取含有token的json
    def request(self):
        try:
            response = requests.post(
                url = self._loginSSO_url,
                headers=self._loginSSO_headers,
                verify=False,
                json=self._loginSSO_body,
            )
            print("success loginSSO")
            return response.json()
        except Exception as e:
            print("loginSSO error:", e)


if __name__ == '__main__':
    request = loginSSO()
    response = request.loginSSO_request()
    print(response.json())
