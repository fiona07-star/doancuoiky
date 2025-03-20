from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QHeaderView

from Spydecat_K24406H.libs.Dataconnector import DataConnector
from Spydecat_K24406H.libs.ExportTool import ExportTool
from Spydecat_K24406H.ui.MainWindowDanhsach import Ui_MainWindow_danh_sach


class MainWindowDanhSachExt(QMainWindow, Ui_MainWindow_danh_sach):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.dc = DataConnector()
        self.khach = self.dc.get_all_khach()
        self.parent = parent  # Lưu cửa sổ gốc (MainWindowCanboExt)

        self.setupSignalAndSlot()
        self.setupTable()
        self.load_data_to_table()


    def setupSignalAndSlot(self):
        self.actionExport_excel.triggered.connect(self.export_to_excel)
        self.actionReturn.triggered.connect(self.return_mainwindow)  # Quay lại màn hình chính

    def setupTable(self):
        """Thiết lập bảng với 6 cột (thêm cột Mã khách)"""
        self.tableWidgetDanhsach.setColumnCount(6)
        self.tableWidgetDanhsach.setHorizontalHeaderLabels(["Mã khách", "Tên", "SĐT", "Email", "Giới tính", "Năm sinh"])
        self.tableWidgetDanhsach.resizeColumnsToContents()

    def load_data_to_table(self):
        """Hiển thị danh sách khách với căn giữa nội dung và giãn đều cột full màn hình."""
        self.khach = self.dc.get_all_khach()  # Đọc lại từ JSON
        self.tableWidgetDanhsach.clearContents()
        self.tableWidgetDanhsach.setRowCount(len(self.khach))

        for row, visitor in enumerate(self.khach):
            # Chuyển đổi giới tính thành "Nam" hoặc "Nữ"
            gioi_tinh = "Nam" if visitor.gioi_tinh in ["Nam", True] else "Nữ"

            # Tạo danh sách các item với nội dung căn giữa
            items = [
                QTableWidgetItem(str(visitor.ma_nguoi_dung)),  # Mã người dùng
                QTableWidgetItem(visitor.ten),  # Tên khách
                QTableWidgetItem(str(visitor.sdt)),  # Số điện thoại
                QTableWidgetItem(visitor.email),  # Email
                QTableWidgetItem(gioi_tinh),  # Giới tính
                QTableWidgetItem(str(visitor.nam_sinh))  # Năm sinh
            ]

            for col, item in enumerate(items):
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Căn giữa nội dung trong ô
                self.tableWidgetDanhsach.setItem(row, col, item)

        # Điều chỉnh kích thước cột để chia đều chiều rộng bảng
        header = self.tableWidgetDanhsach.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  # Chia đều các cột theo toàn bộ chiều rộng

    def export_to_excel(self):
        """Xuất danh sách khách ra file Excel"""
        filename = "../dataset/danhsach_visitors.xlsx"
        extool = ExportTool()
        extool.export_danhsach_khach_to_excel(filename, self.khach)
        QMessageBox.information(self, "Thông báo", "Đã Export Excel thành công")

    def return_mainwindow(self):
        """Quay về cửa sổ chính"""
        if self.parent:  # Kiểm tra nếu parent không phải None
            self.parent.show()  # Hiển thị lại cửa sổ chính
        self.close()  # Đóng cửa sổ danh sách khách
