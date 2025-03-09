from cmcc import *
import time

def main():
    cmcc = CMCC()
    print(cmcc)
    try:
        a = cmcc.login("", "")
    except CMCC.TooManyClientsError as e:
        print("Force login ing")
        a = cmcc.login("", "", True)
    except CMCC.AlreadyLoggedIn as e:
        print("Already logged in")


if __name__ == "__main__":
    while True:
        main()
        time.sleep(1)