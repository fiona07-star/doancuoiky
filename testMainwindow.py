import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from Spydecat_K24406H.ui.MainWindowLuachondoituongExt import MainWindowLuachondoituongExt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = QMainWindow()
    ui = MainWindowLuachondoituongExt()
    ui.setupUi(main_win)
    main_win.show()
    sys.exit(app.exec())
