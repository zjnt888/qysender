import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog,
                             QColorDialog, QFontDialog, QProgressDialog,
                             QLineEdit, QInputDialog, QMessageBox, QWidget)
from PyQt5.QtCore import pyqtSlot, QDir
from ui_Widget import Ui_Form
import pandas as pd
import weixin
from myDialoginface import QmyDialoginface
import os


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.setFixedSize(self.width(), self.height())  # 禁止拉伸窗口大小
        self.df = pd.DataFrame()
        self.winxin = weixin.weixin()


    ##  =================自定义功能函数=================================

        ##  ==========由connectSlotsByName() 自动连接的槽函数===============
    # 获取数据文件的表头备选
    @pyqtSlot()
    def on_btnData_clicked(self):
        curPath = QDir.currentPath()  # 获取系统当前目录
        dlgTitle = "选择一个excle数据文件"  # 对话框标题
        filt = "excle文件(*.xlsx)"  # 文件过滤器
        filename, filtUsed = QFileDialog.getOpenFileName(self, dlgTitle, curPath, filt)
        if len(filename) != 0:
            self.df = pd.read_excel(filename)
            excel_head = self.df.columns.tolist()
            for i in excel_head:
                self.ui.textBrowser.append('{' + i + '}')

    # 更改接口参数
    @pyqtSlot()
    def on_btnInface_clicked(self):
        inface = QmyDialoginface()
        inface.ui.lineEdit_corpid.setText(self.winxin.corpid)
        inface.ui.lineEdit_secret.setText(self.winxin.secret)
        inface.ui.lineEdit_agentid.setText(self.winxin.agentid)
        ret = inface.exec()
        if (ret == QDialog.Accepted):
            corpid, secret, agentid = inface.getinface()
            dic_inface = {'corpid': corpid, 'secret': secret, 'agentid': agentid}
            with open('.//tmp//interface_data.conf', 'w') as f:
                f.write(str(dic_inface))
                f.close()

    @pyqtSlot()
    def on_btnSend_clicked(self):
        das = self.df.to_dict(orient='records')
        for da in das:
            msg = self.ui.plainTextEdit.toPlainText().format(**da)
            usr = da['姓名']
            self.winxin.send_msg(usr, msg)
        dlgTitle = "系统消息"
        strInfo = "发送成功！"
        QMessageBox.about(self, dlgTitle, strInfo)

    @pyqtSlot()  ##"help"
    def on_btnHelp_clicked(self):
        dlgTitle = "使用说明"
        strInfo = "1、点击数据按钮选择excel表格\n2、编辑发送内容\n3、点击发送按钮"
        QMessageBox.about(self, dlgTitle, strInfo)

    @pyqtSlot()  ##"about"
    def on_btnAbout_clicked(self):
        dlgTitle = "关于"
        strInfo = "企业微信数据发送工具V1.0\n仅供测试，如有问题，概不负责！"
        QMessageBox.about(self, dlgTitle, strInfo)


##  =============自定义槽函数===============================


##  ============窗体测试程序 ================================
if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyWidget()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
