from internrtBase import InterNetLogin
import requests

class CCUT(InterNetLogin):
    def __new__(cls, *args, **kwargs):
        if hasattr(cls, "__new__"):
            cls.__instance = super().__new__(cls)
        return cls.__instance

    login_info = {}

    @staticmethod
    def up(wlan_ac_ip, wlan_user_ip, username, password, force=False):
        url = "https://222.28.211.100/"
        headers = {
            "Host": "222.28.211.100",
            "Cache-Control": "max-age=0",
            "Sec-Ch-Ua": '"Chromium";v="133", "Not(A:Brand";v="99"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Linux"',
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Origin": "https://222.28.211.100",
            "Content-Type": "application/x-www-form-urlencoded",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://222.28.211.100/",
            "Accept-Encoding": "gzip, deflate, br",
            "Priority": "u=0, i",
            "Connection": "keep-alive"
        }

        data = {
            "DDDDD": username,
            "upass": password,
            "0MKKey": "123",
            "v6ip": ""
        }

        try:
            response = requests.post(url, headers=headers, data=data)
        except requests.exceptions.ConnectionError|requests.exceptions.ConnectTimeout|requests.exceptions.ReadTimeout:
            print("net work is off")
            return False
        if response.status_code == 200:
            if "msga='userid error2';" in response.text or "msga='userid error1';" in response.text :
                raise CCUT.WrongUsernameOrPassword(username, password)
            elif "msga='set_onlinet error'" in response.text:
                raise CCUT.TooManyClientsError(response.text)
            return True
        return False
        pass