from PyQt6.QtWidgets import QApplication, QMainWindow

from Spydecat_K24406H.ui.LoginMainWindowCanboExt import LoginMainWindowCanboExt

app=QApplication([])
mainwindow=QMainWindow()
myui=LoginMainWindowCanboExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()