from loginLogic import *
import time
from config import *


def try_to_login():
    try:
        username = config.get('username')
        password = config.get('password')
        if not (username or password):
            print("ERR: username or password is missing")
            exit(1)
        return imp_.login(imp_, username, password)
    except internrtBase.WrongUsernameOrPassword as e:
        print("<ERR>:WRONG USERNAME/PASS")
        return False
    except internrtBase.AlreadyLoggedIn as e:
        print("<ERR>:ALREADY LOGGED IN")
        return None
    except internrtBase.NetWorkError as e:
        print("<ERR>:NETWORK ERROR")
        return None
    except internrtBase.FailedGetAcIp as e:
        print("<ERR>:FAILED GET AC IP OR WRONG WIFI CONNECTION")
        exit(1)
    except Exception as e:
        print(e)
        exit(1)
if __name__ == '__main__':
    config = Config()
    imp = config.get('imp')
    if imp is None:
        print("<ERR>:NO IMP")
        exit(1)
    imp_ = None
    try:
        if imp == "CMCC":
            import cmcc
            imp_ = cmcc.CMCC()
        elif imp == "CCUT":
            import ccut
            imp_ = ccut.CCUT()
    except Exception as e:
        print(e)
    if imp_ is None:
        print("<ERR>:IMP NOT SUPPORTED")
        exit(1)

    while True:
        if not stat(imp_):
            if try_to_login():
                print("SUCCESS:LOGGED IN")
        time.sleep(0.5)

