from PyQt6.QtWidgets import QApplication, QMainWindow

from Spydecat_K24406H.ui.MainWindowKhachExt import MainWindowKhachExt

app = QApplication([])
mainwindow = QMainWindow()
myui = MainWindowKhachExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
