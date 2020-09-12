from PyQt5.QtCore import Qt

##from PyQt5.QtCore import  pyqtSlot,Qt

##from PyQt5.QtWidgets import

##from PyQt5.QtGui import
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ui_DialogInface import Ui_DialogInface


class QmyDialoginface(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_DialogInface()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.setFixedSize(self.width(), self.height())  #禁止拉伸窗口

        # self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        # self.setIniSize(rowCount, colCount)

    # ##  ==============自定义功能函数============
    # def setIniSize(self, rowCount, colCount):  ##设置表格大小
    #     self.ui.spin_RwoCount.setValue(rowCount)
    #     self.ui.spin_ColCount.setValue(colCount)
    #
    def getinface(self):  ##以元组数据同时返回行数和列数
        corpid = self.ui.lineEdit_corpid.text()
        secret = self.ui.lineEdit_secret.text()
        agentid = self.ui.lineEdit_agentid.text()
        return corpid, secret, agentid


##  ==========由connectSlotsByName() 自动连接的槽函数==================


##  =============自定义槽函数===============================


##  ============窗体测试程序 ================================
if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyDialoginface()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
