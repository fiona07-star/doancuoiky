# Form implementation generated from reading ui file 'D:\Spydecat_Doancuoiky\Spydecat_K24406H\ui\MainWindowKhach.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_khach_xem_diem(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1384, 775)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\Spydecat_Doancuoiky\\Spydecat_K24406H\\ui\\../images/ic_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 500))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 18pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 0, 109);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setMaximumSize(QtCore.QSize(1500, 800))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(45)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidgetNganh = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidgetNganh.setMaximumSize(QtCore.QSize(500, 150))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listWidgetNganh.setFont(font)
        self.listWidgetNganh.setStyleSheet("background-color: rgb(45, 0, 135);\n"
"font: 12pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.listWidgetNganh.setObjectName("listWidgetNganh")
        self.verticalLayout_3.addWidget(self.listWidgetNganh)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"background-color: rgb(45, 0, 135);\n"
"color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 141, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 121, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 280, 121, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 330, 111, 31))
        self.label_7.setObjectName("label_7")
        self.lineEditPT3 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditPT3.setGeometry(QtCore.QRect(140, 380, 341, 31))
        self.lineEditPT3.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.lineEditPT3.setObjectName("lineEditPT3")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 380, 121, 31))
        self.label_8.setObjectName("label_8")
        self.lineEditPT2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditPT2.setGeometry(QtCore.QRect(140, 330, 341, 31))
        self.lineEditPT2.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"")
        self.lineEditPT2.setObjectName("lineEditPT2")
        self.lineEditPT1B = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditPT1B.setGeometry(QtCore.QRect(140, 280, 341, 31))
        self.lineEditPT1B.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.lineEditPT1B.setObjectName("lineEditPT1B")
        self.lineEditPT1A = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditPT1A.setGeometry(QtCore.QRect(140, 230, 341, 31))
        self.lineEditPT1A.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.lineEditPT1A.setObjectName("lineEditPT1A")
        self.lineEditMatuyensinh = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditMatuyensinh.setGeometry(QtCore.QRect(140, 130, 341, 31))
        self.lineEditMatuyensinh.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.lineEditMatuyensinh.setObjectName("lineEditMatuyensinh")
        self.lineEditChuyennganh = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditChuyennganh.setGeometry(QtCore.QRect(140, 80, 341, 31))
        self.lineEditChuyennganh.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.lineEditChuyennganh.setObjectName("lineEditChuyennganh")
        self.lineEditNganhtuyensinh = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditNganhtuyensinh.setGeometry(QtCore.QRect(140, 30, 341, 31))
        self.lineEditNganhtuyensinh.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.lineEditNganhtuyensinh.setObjectName("lineEditNganhtuyensinh")
        self.lineEditChitieu = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditChitieu.setGeometry(QtCore.QRect(140, 180, 341, 31))
        self.lineEditChitieu.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.lineEditChitieu.setObjectName("lineEditChitieu")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 180, 121, 31))
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(500, 85))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 0, 135);\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButtonTimhieuthem = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonTimhieuthem.setGeometry(QtCore.QRect(20, 30, 151, 41))
        self.pushButtonTimhieuthem.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\Spydecat_Doancuoiky\\Spydecat_K24406H\\ui\\../images/ic_find.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonTimhieuthem.setIcon(icon1)
        self.pushButtonTimhieuthem.setObjectName("pushButtonTimhieuthem")
        self.pushButtonThoat = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonThoat.setGeometry(QtCore.QRect(360, 30, 121, 41))
        self.pushButtonThoat.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\Spydecat_Doancuoiky\\Spydecat_K24406H\\ui\\../images/ic_exitt.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonThoat.setIcon(icon2)
        self.pushButtonThoat.setObjectName("pushButtonThoat")
        self.pushButtonLienhetuvan = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonLienhetuvan.setGeometry(QtCore.QRect(190, 30, 151, 41))
        self.pushButtonLienhetuvan.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("D:\\Spydecat_Doancuoiky\\Spydecat_K24406H\\ui\\../images/ic_contact.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonLienhetuvan.setIcon(icon3)
        self.pushButtonLienhetuvan.setObjectName("pushButtonLienhetuvan")
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1384, 26))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHint = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("D:\\Spydecat_Doancuoiky\\Spydecat_K24406H\\ui\\../images/ic_hint.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionHint.setIcon(icon4)
        self.actionHint.setObjectName("actionHint")
        self.menuHelp.addAction(self.actionHint)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Màn hình khách"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">HỆ THỐNG QUẢN LÝ THÔNG TIN TUYỂN SINH</span></p></body></html>"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ngành tuyển sinh"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Chuyên ngành"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mã tuyển sinh"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Chỉ tiêu"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Phương thức 1A"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Phương thức 1B"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Phương thức 2"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Phương thức 3"))
        self.groupBox.setTitle(_translate("MainWindow", "Thông tin chi tiết:"))
        self.label_2.setText(_translate("MainWindow", "Chuyên ngành:"))
        self.label_3.setText(_translate("MainWindow", "Ngành tuyển sinh:"))
        self.label_4.setText(_translate("MainWindow", "Mã tuyển sinh:"))
        self.label_5.setText(_translate("MainWindow", "Phương thức 1A:"))
        self.label_6.setText(_translate("MainWindow", "Phương thức 1B:"))
        self.label_7.setText(_translate("MainWindow", "Phương thức 2:"))
        self.label_8.setText(_translate("MainWindow", "Phương thức 3:"))
        self.label_9.setText(_translate("MainWindow", "Chỉ tiêu:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Thao tác:"))
        self.pushButtonTimhieuthem.setText(_translate("MainWindow", "Tìm hiểu thêm"))
        self.pushButtonThoat.setText(_translate("MainWindow", "Thoát"))
        self.pushButtonLienhetuvan.setText(_translate("MainWindow", "Liên hệ tư vấn"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionHint.setText(_translate("MainWindow", "Hint"))
        self.actionHint.setShortcut(_translate("MainWindow", "Ctrl+T"))
