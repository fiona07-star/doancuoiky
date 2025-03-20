from PyQt6.QtWidgets import QMainWindow

from Spydecat_K24406H.ui.LoginMainWindowCanboExt import LoginMainWindowCanboExt
from Spydecat_K24406H.ui.LoginMainWindowKhachExt import LoginMainWindowKhachExt
from Spydecat_K24406H.ui.MainWindowLuachondoituong import Ui_MainWindow_lua_chon


class MainWindowLuachondoituongExt(Ui_MainWindow_lua_chon):
    def __init__(self):
        self.new_window = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        self.pushButtonKhach.clicked.connect(self.toi_la_khach)
        self.pushButtonCanbo.clicked.connect(self.toi_la_can_bo)

    def toi_la_khach(self):
        self.MainWindow.hide()
        self.new_window = QMainWindow()
        self.ui = LoginMainWindowKhachExt()
        self.ui.setupUi(self.new_window)
        self.new_window.show()

    def toi_la_can_bo(self):
        self.MainWindow.hide()
        self.new_window = QMainWindow()
        self.ui = LoginMainWindowCanboExt()
        self.ui.setupUi(self.new_window)
        self.new_window.show()
