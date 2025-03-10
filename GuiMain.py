
from PySide6.QtWidgets import QApplication, QWidget

from GuiResource.GuiWin import Ui_dialog
from GuiLogic import GuiLogics


# 定义窗口类
class Mainwindow(QWidget, Ui_dialog,GuiLogics):
    def __init__(self):  # 继承窗口和win文件中的Ui_From类
        super().__init__()
        self.setupUi(self)  # 导入UI文件
        self.button_bind()


    def button_bind(self):
        self.OKButton.clicked.connect(self.createJson)
        self.NoButton.clicked.connect(self.closeWin)



if __name__ == "__main__":
    app = QApplication([])  # 开启，传参
    windows = Mainwindow()  # 实例化对象
    windows.show()  # 显示窗口
    app.exec()  # 循环监听