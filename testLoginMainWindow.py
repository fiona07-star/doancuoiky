from PyQt6.QtWidgets import QApplication, QMainWindow

from Spydecat_K24406H.ui.MainWindowDanhSachExt import MainWindowDanhSachExt

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowDanhSachExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()