# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GuiWin.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)
from . import GuiResource_rc

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.setWindowModality(Qt.WindowModality.WindowModal)
        dialog.resize(486, 367)
        dialog.setMaximumSize(QSize(486, 367))
        icon = QIcon()
        icon.addFile(u":/icos/\u5c0f\u732b.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        dialog.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.title = QLabel(dialog)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 80))
        font = QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.title, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.OKButton = QPushButton(dialog)
        self.OKButton.setObjectName(u"OKButton")
        self.OKButton.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_2.addWidget(self.OKButton)

        self.NoButton = QPushButton(dialog)
        self.NoButton.setObjectName(u"NoButton")
        self.NoButton.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_2.addWidget(self.NoButton)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 49)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.userLabel = QLabel(dialog)
        self.userLabel.setObjectName(u"userLabel")

        self.horizontalLayout.addWidget(self.userLabel)

        self.userLine = QLineEdit(dialog)
        self.userLine.setObjectName(u"userLine")

        self.horizontalLayout.addWidget(self.userLine)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 64, -1, 79)
        self.label_3 = QLabel(dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.CMCCButton = QRadioButton(dialog)
        self.CMCCButton.setObjectName(u"CMCCButton")

        self.horizontalLayout_3.addWidget(self.CMCCButton)

        self.CCUTButton = QRadioButton(dialog)
        self.CCUTButton.setObjectName(u"CCUTButton")

        self.horizontalLayout_3.addWidget(self.CCUTButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pwdLabel = QLabel(dialog)
        self.pwdLabel.setObjectName(u"pwdLabel")

        self.horizontalLayout_2.addWidget(self.pwdLabel)

        self.pwdLine = QLineEdit(dialog)
        self.pwdLine.setObjectName(u"pwdLine")

        self.horizontalLayout_2.addWidget(self.pwdLine)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.autoStart = QCheckBox(dialog)
        self.autoStart.setObjectName(u"autoStart")

        self.gridLayout.addWidget(self.autoStart, 1, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)

        self.author = QLabel(dialog)
        self.author.setObjectName(u"author")
        self.author.setMaximumSize(QSize(16777215, 30))
        self.author.setTextFormat(Qt.TextFormat.AutoText)
        self.author.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.author.setWordWrap(True)

        self.gridLayout_2.addWidget(self.author, 2, 0, 1, 2)


        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"\u5de5\u5927\u6821\u56ed\u7f51\u7edc\u767b\u5f55\u81ea\u52a8\u5316\u914d\u7f6e\u5668", None))
        self.title.setText(QCoreApplication.translate("dialog", u"\u5de5\u5927\u6821\u56ed\u7f51\u767b\u5f55\u81ea\u52a8\u5316\u914d\u7f6e\u5668", None))
        self.OKButton.setText(QCoreApplication.translate("dialog", u"\u786e\u5b9a", None))
        self.NoButton.setText(QCoreApplication.translate("dialog", u"\u53d6\u6d88", None))
        self.userLabel.setText(QCoreApplication.translate("dialog", u"\u8d26\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("dialog", u"\u8981\u767b\u9646\u7684\u7f51\u7edc", None))
        self.CMCCButton.setText(QCoreApplication.translate("dialog", u"CMCC", None))
        self.CCUTButton.setText(QCoreApplication.translate("dialog", u"CCUT", None))
        self.pwdLabel.setText(QCoreApplication.translate("dialog", u"\u5bc6\u7801", None))
        self.autoStart.setText(QCoreApplication.translate("dialog", u"\u5f00\u673a\u81ea\u542f\u52a8", None))
        self.author.setText(QCoreApplication.translate("dialog", u"<html><head/><body><p>\u4f5c\u8005:\u7fa4\u7537\u5a18\uff0c\u5317\u5cad\u5927\u5e05\u732b</p></body></html>", None))
    # retranslateUi

