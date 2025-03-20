from PyQt6.QtWidgets import QApplication, QMainWindow

from Spydecat_K24406H.ui.MainWindowCanboExt import MainWindowCanboExt

app = QApplication([])
mainwindow = QMainWindow()
myui = MainWindowCanboExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
