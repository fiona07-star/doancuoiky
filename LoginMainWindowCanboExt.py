import random
import string
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QApplication

from Spydecat_K24406H.libs.Dataconnector import DataConnector
from Spydecat_K24406H.ui.LoginMainWindowCanbo import Ui_MainWindow_can_bo_dang_nhap
from Spydecat_K24406H.ui.MainWindowCanboExt import MainWindowCanboExt


class LoginMainWindowCanboExt(Ui_MainWindow_can_bo_dang_nhap):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
        self.MainWindow.show()  #Hiển thị trước khi cập nhật UI
        self.generate_captcha()  #Tạo captcha khi mở giao diện

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)
        self.pushButtonExit.clicked.connect(self.thoat)
        self.pushButtonCaptcha.clicked.connect(self.generate_captcha)  # Làm mới captcha

    def generate_captcha(self):
        """Tạo Captcha mới và cập nhật giao diện"""
        characters = string.ascii_letters + string.digits  # Chữ hoa, chữ thường, số
        self.captcha_text = ''.join(random.choices(characters, k=6))  # Captcha 6 ký tự
        print(f"🔹 Captcha mới: {self.captcha_text}")  # Debug kiểm tra

        # Hiển thị Captcha trong `lineEditCaptcha` (Không cho sửa)
        self.lineEditCaptcha.setText(self.captcha_text)
        self.lineEditCaptcha.setReadOnly(True)

        # Xóa ô nhập Captcha cũ của người dùng
        self.lineEditEnterCaptcha.clear()
        self.lineEditEnterCaptcha.setFocus()  # Chuyển con trỏ nhập vào đây

    def thoat(self):
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Bạn có chắc muốn thoát?")
        msgbox.setWindowTitle("Xác nhận thoát")
        msgbox.setIcon(QMessageBox.Icon.Warning)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgbox.setStandardButtons(buttons)

        if msgbox.exec() == QMessageBox.StandardButton.Yes:
            QApplication.quit()

    def process_login(self):
        dc = DataConnector()
        uid = self.lineEditEmail.text().strip()
        pwd = self.lineEditPassword.text().strip()
        user_captcha = self.lineEditEnterCaptcha.text().strip()  # Captcha người nhập
        real_captcha = self.captcha_text  # Captcha hệ thống sinh

        # Nếu Captcha nhập sai, dừng ngay lập tức
        if user_captcha != real_captcha:
            QMessageBox.warning(self.MainWindow, "Đăng nhập thất bại", "Captcha không đúng! Vui lòng thử lại.")
            self.generate_captcha()  # Làm mới Captcha khi sai
            return  # Dừng lại, không kiểm tra tiếp

        # Nếu Captcha đúng, kiểm tra tài khoản
        emp = dc.login(uid, pwd)

        if emp is not None:
            self.MainWindow.close()  # Đóng cửa sổ đăng nhập

            # Mở MainWindowCanboExt
            self.new_window = QMainWindow()
            self.ui = MainWindowCanboExt()  # Dùng lớp mở rộng
            self.ui.setupUi(self.new_window)  # Khởi tạo giao diện
            self.new_window.show()  # Hiển thị cửa sổ chính
        else:
            QMessageBox.warning(self.MainWindow, "Đăng nhập thất bại", "Email hoặc mật khẩu không đúng!")

