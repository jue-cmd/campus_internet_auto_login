from login.config import get_config
from GuiResource.InfoPop import MessagePopup

class GuiLogics():
    def closeWin(self):
        self.close()

    def createJson(self):

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