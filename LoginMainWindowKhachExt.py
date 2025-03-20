from PyQt6.QtWidgets import QMainWindow, QMessageBox

from Spydecat_K24406H.libs.Dataconnector import DataConnector
from Spydecat_K24406H.models.Khach import Khach
from Spydecat_K24406H.ui.LoginMainWindowKhach import Ui_MainWindow_khach_nhap_thong_tin
from Spydecat_K24406H.ui.MainWindowKhachExt import MainWindowKhachExt


class LoginMainWindowKhachExt(Ui_MainWindow_khach_nhap_thong_tin):
    def __init__(self):
        self.new_window = None
        self.dc=DataConnector()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        self.pushButtonLuu.clicked.connect(self.save)
        self.pushButtonThoat.clicked.connect(self.exit_program)

    def save(self):
        ten = self.lineEditHovaten.text().strip()
        nam_sinh = self.lineEditNamsinh.text().strip()
        email = self.lineEditEmail.text().strip()
        sdt = self.lineEditSodienthoai.text().strip()

        # Kiểm tra radio button
        if self.radioButtonNam.isChecked():
            gioi_tinh = "Nam"
        elif self.radioButtonNu.isChecked():
            gioi_tinh = "Nữ"
        else:
            QMessageBox.warning(self.MainWindow, "Thiếu thông tin", "Vui lòng chọn giới tính!")
            return

        # Kiểm tra nếu có bất kỳ ô nào trống
        if not ten or not nam_sinh or not email or not sdt:
            QMessageBox.warning(self.MainWindow, "Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin!")
            return

        # In ra để kiểm tra
        print(f"Tên: {ten}, Năm sinh: {nam_sinh}, Email: {email}, SĐT: {sdt}, Giới tính: {gioi_tinh}")
        # Lấy mã khách tự động
        ma_khach = self.dc.get_next_khach_id()
        # Lưu thông tin khách vào JSON
        khach_moi = Khach(ma_nguoi_dung=ma_khach, ten=ten, nam_sinh=str(nam_sinh), email=email, sdt=sdt,
                          gioi_tinh=gioi_tinh)
        self.dc.save_new_khach(khach_moi)

        # Nếu đã nhập đủ, chuyển qua MainWindowKhachExt
        self.MainWindow.hide()  # Ẩn cửa sổ đăng nhập

        # Tạo cửa sổ mới
        self.main_window = QMainWindow()
        self.new_window = MainWindowKhachExt()  # Không truyền tham số
        self.new_window.setupUi(self.main_window)
        self.main_window.show()

    def exit_program(self):
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Bạn có chắc muốn thoát?")
        msgbox.setWindowTitle("Xác nhận thoát")
        msgbox.setIcon(QMessageBox.Icon.Critical)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgbox.setStandardButtons(buttons)

        if msgbox.exec() == QMessageBox.StandardButton.Yes:
            exit()
