##  GUI应用程序主程序入口

import sys,os

from PyQt5.QtWidgets import QApplication
# from PyQt5.QtGui import  QIcon
from PyQt5.QtWidgets import QMessageBox
from myWidget import QmyWidget


app = QApplication(sys.argv)  # 创建GUI应用程序
##icon = QIcon(":/icons/images/app.ico")
##app.setWindowIcon(icon)

# 判断tmp目录下是否存在联系人和接口数据文件
if not os.path.exists("tmp/addressbook.xlsx"):
    msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有找到联系人文件addressbook.xlsx，请检查tmp目录')
    msg_box.exec_()
elif not os.path.exists("tmp/interface_data.conf"):
    msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有找到接口数据文件interface_data.conf，请检查tmp目录')
    msg_box.exec_()
else:
    mainform = QmyWidget()  # 创建主窗体
    mainform.show()  # 显示主窗体
    sys.exit(app.exec_())

