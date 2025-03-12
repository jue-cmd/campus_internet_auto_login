from cmcc import *
from ccut import *
import time
import json

def main():
    confs=json.load(open('confs.json'))
    confs=json.loads(confs)
    print(confs)
    if confs['autostart']:
        if confs['type']=='CMCC':
            cmcc = CMCC()
            print(cmcc)
            try:
                a = cmcc.login(confs['user'],confs['pwd'], "")
            except CMCC.TooManyClientsError as e:
                print("Force login ing")
                a = cmcc.login(confs['user'], confs['pwd'], True)
            except CMCC.AlreadyLoggedIn as e:
                print("Already logged in")
        elif confs['type']=='CCUT':
            ccut = CCUT()
            print(ccut)
            try:
                a = ccut.login(confs['user'],confs['pwd'])
            except CMCC.TooManyClientsError as e:
                print("Force login ing")
                a = ccut.login(confs['user'],confs['pwd'], True)
            except CMCC.AlreadyLoggedIn as e:
                print("Already logged in")


if __name__ == "__main__":
    main()