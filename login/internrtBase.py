import requests
from abc import abstractmethod

class WrongUsernameOrPassword(RuntimeError):
    def __init__(self, username, password):
        self.username = username
        self.password = password


class NetWorkError(RuntimeError):
    def __init__(self, message):
        self.message = message


class TooManyClientsError(RuntimeError):
    def __init__(self, message):
        self.message = message


class FailedGetAcIp(RuntimeError):
    def __init__(self, message):
        self.message = message


class AlreadyLoggedIn(RuntimeError):
    def __init__(self, username, password):
        self.username = username
        self.password = password

class NotLoggedIn(RuntimeError):
    def __init__(self):
        print("666")

class InterNetLogin:

    login_session=None

    @staticmethod
    @abstractmethod
    def up(wlan_ac_ip, wlan_user_ip, username, password, force=False):
        pass
    @staticmethod
    @abstractmethod
    def down(wlan_ac_ip, wlan_user_ip):
        pass
    @staticmethod
    @abstractmethod
    def get_ac_and_your_ip()-> dict | bool:
        pass

    @abstractmethod
    def login(self, username, password)->bool|dict:
        pass

    @abstractmethod
    def logout(self):
        pass

    @staticmethod
    def check_internet_connection():
        header = {
            "Upgrade-Insecure-Requests": "1"
        }
        responses = requests.get("http://networkcheck.kde.org/", headers=header, allow_redirects=False)
        if responses.status_code != 200:
            return False
        if responses.text != "OK":
            return False
        return True
