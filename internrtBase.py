class InterNetLogin():
    class WrongUsernameOrPassword(RuntimeError):
        def __init__(self,username,password):
            self.username = username
            self.password = password
    class NetWorkError(RuntimeError):
        def __init__(self,message):
            self.message = message
    class TooManyClientsError(RuntimeError):
        def __init__(self,message):
            self.message = message
    class FailedGetAcIp(RuntimeError):
        def __init__(self,message):
            self.message = message

    class AlreadyLoggedIn(RuntimeError):
        def __init__(self,username,password):
            self.username = username
            self.password = password
    @staticmethod
    def up(wlan_ac_ip, wlan_user_ip, username, password, force=False):
        pass
    @staticmethod
    def down(wlan_ac_ip, wlan_user_ip):
        pass
    @staticmethod
    def get_ac_and_your_ip()-> dict | bool:
        pass
    def login(self, username, password)->bool|dict:
        pass