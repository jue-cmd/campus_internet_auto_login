import requests
from internrtBase import InterNetLogin


class CMCC(InterNetLogin):
    def __new__(cls, *args, **kwargs):
        if hasattr(cls, "__new__"):
            cls.__instance = super().__new__(cls)
        return cls.__instance

    login_info = {}
    server_ip=""
    @staticmethod
    def down(wlan_ac_ip, wlan_user_ip)-> bool:
        # 目标 URL
        url = "http://111.26.29.113:7119/portalLogout.wlan?44444&isCloseWindow=N"
        # 请求头
        headers = {
            "Host": "111.26.29.113:7119",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "http://111.26.29.113:7119/portalLoginRedirect.wlan",
            "Cookie": "theme_name=THEME_PC",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        # 请求体（表单数据）
        data = {
            "wlanAcName": "",
            "wlanAcIp": wlan_ac_ip,
            "wlanUserIp": wlan_user_ip,
            "ssid": "edu",
            "userName": "114514ccut",
            "logonsessid": "",
            "encryUser": "",
            "booktime": "",
            "validperiod": "",
            "passType": "1",
            "cookies": "",
            "isLocalUser": "",
        }

        # 发送 POST 请求
        response = requests.post(url, headers=headers, data=data)

        # 输出响应
        if response.status_code != 200:
            raise Exception("net error")
        if "下线成功" in response.text:
            return True
        else:
            return False

    @staticmethod
    def up(wlan_ac_ip, wlan_user_ip, username, password, force=False)->bool:

        headers = {
            'Cache-Control': 'max-age=0',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Origin': 'http://111.26.29.113:7119',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Referer': 'http://111.26.29.113:7119/portal.wlan?wlanacname=&wlanacip=211.137.223.239&wlanuserip=100.125.66.232&ssid=edu',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }

        data = {
            'wlanAcName': '',
            'wlanAcIp': wlan_ac_ip,
            'wlanUserIp': wlan_user_ip,
            'ssid': 'edu',
            'passType': '1',
            'userName': username,
            'userPwd': password,
            'onlineInfo': '',
            'saveUser': ''
        }

        url = "http://111.26.29.113:7119/portalLogin.wlan"

        if force:
            url = "http://111.26.29.113:7119/portalForceLogin.wlan"
            headers["Referer"] = "http://111.26.29.113:7119/portalLogin.wlan"

        try:
            response = requests.post(url, headers=headers, data=data)
        except requests.exceptions.ConnectionError|requests.exceptions.ConnectTimeout|requests.exceptions.ReadTimeout:
            print("net work is off")
            return False
        if response.status_code == 200:
            if "登录认证失败，用户名或密码错误" in response.text:
                raise CMCC.WrongUsernameOrPassword(username, password)
            elif "您好，您当前登录的用户已在线，是否继续操作？" in response.text:
                raise CMCC.TooManyClientsError(response.text)
            return True
        return False

    # get ac info
    @staticmethod
    def get_ac_and_your_ip() -> dict | bool:
        header = {
            "Upgrade-Insecure-Requests": "1"
        }
        responses = requests.get("http://networkcheck.kde.org/", headers=header, allow_redirects=False)
        print(responses.text)
        if responses.status_code == 302:
            print(responses.headers)
            data: str = responses.headers["Location"]
            if data:
                try:
                    datas = data.split("?")[1].split("&")
                    return {
                        "ac_ip": datas[2].split("=")[1],
                        "your_ip": datas[0].split("=")[1],
                        "login_url":data.split("?")[0]
                    }
                except:
                    raise CMCC.FailedGetAcIp(data)
        if responses.status_code == 200:
            if "OK" in responses.text:
                return True
        return False

    def login(self, username, password, force=False)->bool|dict:
        ip = self.get_ac_and_your_ip()
        if type(ip) == dict:
            ret = self.up(ip["ac_ip"], ip["your_ip"], username, password, force)
            if ret:
                self.login_info = ip
                return self.login_info
        else:
            raise CMCC.AlreadyLoggedIn(username, password)
        return False
