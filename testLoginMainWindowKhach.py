from PyQt6.QtWidgets import QApplication, QMainWindow

from Spydecat_K24406H.ui.LoginMainWindowKhachExt import LoginMainWindowKhachExt

app=QApplication([])
mainwindow=QMainWindow()
myui=LoginMainWindowKhachExt()
myui.setupUi(mainwindow)
myui.show()
app.exec()