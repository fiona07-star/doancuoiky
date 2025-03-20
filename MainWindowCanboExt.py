import os
import webbrowser

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidgetItem, QTableWidgetItem, QMessageBox, QHeaderView

from Spydecat_K24406H.libs.Dataconnector import DataConnector
from Spydecat_K24406H.libs.ExportTool import ExportTool
from Spydecat_K24406H.models.Nganh_hoc import Nganh_hoc
from Spydecat_K24406H.ui.MainWindowCanbo import Ui_MainWindow_quan_ly_diem
from Spydecat_K24406H.ui.MainWindowDanhSachExt import MainWindowDanhSachExt


class MainWindowCanboExt(Ui_MainWindow_quan_ly_diem):
    def __init__(self):
        self.dc = DataConnector()
        self.all_nganh_hoc = ExportTool().import_bang_diem_from_excel("../dataset/Bangdiem.xlsx")
        self.nganh_hoc=self.all_nganh_hoc
        self.chuyen_nganh = self.dc.get_chuyen_nganh_by_nganh_hoc(self.nganh_hoc[0].ten_nganh if self.nganh_hoc else "")
        self.selected_nganh = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.show_chuyen_nganh_gui()
        self.show_nganh_hoc_gui()
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def show_chuyen_nganh_gui(self):
        self.listWidgetNganh.clear()

        # Thêm dòng "Tất cả ngành học"
        self.listWidgetNganh.addItem("Tất cả ngành học")

        # Dùng set để loại bỏ ngành trùng lặp
        unique_nganh = set(nganh.ten_nganh for nganh in self.all_nganh_hoc)

        for ten_nganh in unique_nganh:
            item = QListWidgetItem(ten_nganh)
            self.listWidgetNganh.addItem(item)

    def show_nganh_hoc_gui(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(self.nganh_hoc))

        # Căn chỉnh cột theo nội dung
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        for row, nganh in enumerate(self.nganh_hoc):
            col_ten_nganh = QTableWidgetItem(nganh.ten_nganh if nganh.ten_nganh else "N/A")
            col_chuyen_nganh = QTableWidgetItem(nganh.chuyen_nganh if nganh.chuyen_nganh else "N/A")
            col_ma_tuyen_sinh = QTableWidgetItem(nganh.ma_tuyen_sinh if nganh.ma_tuyen_sinh else "N/A")
            col_chi_tieu = QTableWidgetItem(str(nganh.chi_tieu) if nganh.chi_tieu else "0")
            col_pt1a = QTableWidgetItem(str(nganh.phuong_thuc_1a) if nganh.phuong_thuc_1a else "0")
            col_pt1b = QTableWidgetItem(str(nganh.phuong_thuc_1b) if nganh.phuong_thuc_1b else "0")
            col_pt2 = QTableWidgetItem(str(nganh.phuong_thuc_2) if nganh.phuong_thuc_2 else "0")
            col_pt3 = QTableWidgetItem(str(nganh.phuong_thuc_3) if nganh.phuong_thuc_3 else "0")

            items = [col_ten_nganh, col_chuyen_nganh, col_ma_tuyen_sinh, col_chi_tieu, col_pt1a, col_pt1b, col_pt2,
                     col_pt3]

            for col, item in enumerate(items):
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Căn giữa nội dung
                self.tableWidget.setItem(row, col, item)

        # Tự động điều chỉnh hàng theo nội dung
        self.tableWidget.resizeRowsToContents()

        print("TableWidget đã được cập nhật với dữ liệu mới.")

    def setupSignalAndSlot(self):
        self.listWidgetNganh.itemSelectionChanged.connect(self.filter_nganh)
        self.tableWidget.itemSelectionChanged.connect(self.show_detail_nganh)
        self.pushButtonClearAll.clicked.connect(self.them_nganh_hoc_detail)
        self.pushButtonSave.clicked.connect(self.luu_nganh)
        self.pushButtonDelete.clicked.connect(self.xoa_nganh)
        self.actionExport_Excel.triggered.connect(self.export_bang_diem_to_excel)
        self.actionImport_Excel.triggered.connect(self.import_bang_diem_from_excel)
        self.actionExit.triggered.connect(self.exit_program)
        self.actionCurrent_help.triggered.connect(self.open_help)
        self.actionList_of_Visitors.triggered.connect(self.danh_sach_khach)
        self.actionHint.triggered.connect(self.thong_tin_chi_tiet)

    def filter_nganh(self):
        row = self.listWidgetNganh.currentRow()
        ten_nganh = self.listWidgetNganh.currentItem().text()

        if ten_nganh == "Tất cả ngành học":
            self.nganh_hoc = self.all_nganh_hoc  # Hiển thị toàn bộ ngành
        else:
            self.nganh_hoc = [nganh for nganh in self.all_nganh_hoc if nganh.ten_nganh == ten_nganh]

        self.show_nganh_hoc_gui()

    def show_detail_nganh(self):
        index = self.tableWidget.currentRow()
        if index < 0 or index >= len(self.nganh_hoc):  # Kiểm tra index hợp lệ
            return

        nganh = self.nganh_hoc[index]  # Tránh lỗi out of range

        self.lineEditNganhtuyensinh.setText(nganh.ten_nganh)
        self.lineEditChuyennganh.setText(nganh.chuyen_nganh)
        self.lineEditMatuyensinh.setText(str(nganh.ma_tuyen_sinh))
        self.lineEditChitieu.setText(str(nganh.chi_tieu))
        self.lineEditPT1A.setText(str(nganh.phuong_thuc_1a))
        self.lineEditPT1B.setText(str(nganh.phuong_thuc_1b))
        self.lineEditPT2.setText(str(nganh.phuong_thuc_2))
        self.lineEditPT3.setText(str(nganh.phuong_thuc_3))

    def them_nganh_hoc_detail(self):
        self.lineEditNganhtuyensinh.clear()
        self.lineEditChuyennganh.clear()
        self.lineEditMatuyensinh.clear()
        self.lineEditChitieu.clear()
        self.lineEditPT1A.clear()
        self.lineEditPT1B.clear()
        self.lineEditPT2.clear()
        self.lineEditPT3.clear()
        self.lineEditNganhtuyensinh.setFocus()

    def luu_nganh(self):
        ten_nganh = self.lineEditNganhtuyensinh.text()
        chuyen_nganh = self.lineEditChuyennganh.text()
        ma_tuyen_sinh = self.lineEditMatuyensinh.text()
        chi_tieu = self.lineEditChitieu.text()
        pt1a = self.lineEditPT1A.text()
        pt1b = self.lineEditPT1B.text()
        pt2 = self.lineEditPT2.text()
        pt3 = self.lineEditPT3.text()

        # Tạo đối tượng ngành học mới
        nganh_hoc = Nganh_hoc(ten_nganh, chuyen_nganh, ma_tuyen_sinh, chi_tieu, pt1a, pt1b, pt2, pt3)

        index = self.tableWidget.currentRow()

        if index < 0:  # Nếu không có dòng nào được chọn -> Thêm mới
            self.nganh_hoc.append(nganh_hoc)
        else:  # Nếu có dòng được chọn -> Cập nhật
            self.nganh_hoc[index] = nganh_hoc

        # Ghi đè dữ liệu mới vào JSON
        self.dc.save_nganh_hoc_to_json(self.nganh_hoc)

        # Cập nhật lại giao diện
        self.show_nganh_hoc_gui()

    def xoa_nganh(self):
        index = self.tableWidget.currentRow()
        if index < 0:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một ngành học để xóa!")
            return

        chuyen_nganh = self.lineEditChuyennganh.text()  # Lấy chuyên ngành từ lineEdit

        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText(f"Bạn có chắc muốn xóa ngành {chuyen_nganh} không?")
        msgbox.setWindowTitle("Xác nhận xóa")
        msgbox.setIcon(QMessageBox.Icon.Warning)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgbox.setStandardButtons(buttons)

        if msgbox.exec() == QMessageBox.StandardButton.Yes:
            # Xóa trong danh sách nganh_hoc
            self.nganh_hoc.pop(index)

            # Ghi đè dữ liệu mới vào JSON
            self.dc.save_nganh_hoc_to_json(self.nganh_hoc)

            # Cập nhật lại bảng
            self.show_nganh_hoc_gui()

    def exit_program(self):
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Bạn có chắc muốn thoát không?")
        msgbox.setWindowTitle("Xác nhận thoát")
        msgbox.setIcon(QMessageBox.Icon.Critical)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgbox.setStandardButtons(buttons)
        if msgbox.exec() == QMessageBox.StandardButton.Yes:
            exit()

    def export_bang_diem_to_excel(self):
        filename = "../dataset/Bangdiem.xlsx"
        extool = ExportTool()
        extool.export_bang_diem_to_excel(filename, self.nganh_hoc)
        QMessageBox.information(self.MainWindow, "Thông báo", "Đã xuất file Excel thành công")

    def import_bang_diem_from_excel(self):
        print("Hàm import_bang_diem_from_excel() đã được gọi!")  # Debug
        filename = "../dataset/Bangdiem.xlsx"
        extool = ExportTool()

        # Import dữ liệu mới
        self.nganh_hoc = extool.import_bang_diem_from_excel(filename)

        # Ghi đè dữ liệu mới vào JSON
        self.dc.save_nganh_hoc_to_json(self.nganh_hoc)

        # Cập nhật giao diện
        self.show_chuyen_nganh_gui()
        self.show_nganh_hoc_gui()

    def open_help(self):
        file_help = "HELP.pdf"
        current_path = os.getcwd()
        file_help = f"{current_path}/../dataset/{file_help}"
        webbrowser.open_new(file_help)

    def danh_sach_khach(self):
        """Mở màn hình danh sách khách"""
        self.MainWindow.hide()  # Ẩn cửa sổ chính
        self.danh_sach_window = MainWindowDanhSachExt(parent=self.MainWindow)  # Truyền QMainWindow làm parent
        self.danh_sach_window.show()

    def thong_tin_chi_tiet(self):
        file_hint = "HINT.pdf"
        current_path = os.getcwd()
        file_hint = f"{current_path}/../dataset/{file_hint}"
        webbrowser.open_new(file_hint)