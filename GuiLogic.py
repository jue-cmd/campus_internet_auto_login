import json
from GuiResource.InfoPop import MessagePopup

class GuiLogics():
    def closeWin(self):
        self.close()

    def createJson(self):
        self.confs={
            'user':'',
            'pwd':'',
            'type':'',
            'autostart':False
        }
        self.confs['user']=self.userLine.text()
        self.confs['pwd']=self.pwdLine.text()
        if not self.judgeType():
            return False
        if self.autoStart.isChecked():
            self.confs['autostart']=True
        self.json=json.dumps(self.confs)
        with open("login/confs.json", "w") as f:
            json.dump(self.json, f)
        self.pop = MessagePopup("配置完成!!")
        self.pop.show()


    def judgeType(self):
        #类型判断
        if self.CMCCButton.isChecked():
            self.confs['type'] = 'CMCC'
        elif self.CCUTButton.isChecked():
            self.confs['type'] = 'CCUT'
        else:
            self.pop=MessagePopup("别瞎搞啊！！选择你连接哪个网啊！！")
            self.pop.show()
            return False
        return True



if __name__ == '__main__':
    print("ok")