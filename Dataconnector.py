import os
import json

from Spydecat_K24406H.libs.JsonFileFactory import JsonFileFactory
from Spydecat_K24406H.models.CBNV import Canbo
from Spydecat_K24406H.models.Khach import Khach
from Spydecat_K24406H.models.Nganh_hoc import Nganh_hoc


class DataConnector:
    def __init__(self):
        """ Khởi tạo đối tượng và đặt đường dẫn file JSON """
        self.json_factory = JsonFileFactory()
        self.file_cbnv = os.path.join("..", "dataset", "cbnv.json")
        self.file_khach = os.path.join("..", "dataset", "khach.json")
        self.file_nganh_hoc = os.path.join("..", "dataset", "nganh_hoc.json")

    def get_all_cbnv(self):
        """ Đọc danh sách cán bộ từ file JSON """
        return self.json_factory.read_data(self.file_cbnv, Canbo)

    def get_all_khach(self):
        """ Đọc danh sách khách từ file JSON """
        return self.json_factory.read_data(self.file_khach, Khach)

    def get_all_nganh_hoc(self):
        """ Đọc danh sách ngành học từ file JSON """
        return self.json_factory.read_data(self.file_nganh_hoc, Nganh_hoc)

    def login(self, email, mat_khau):
        """ Kiểm tra đăng nhập """
        return next((cb for cb in self.get_all_cbnv() if cb.email == email and cb.mat_khau == mat_khau), None)

    def get_chuyen_nganh_by_nganh_hoc(self, ten_nganh):
        """ Lọc danh sách chuyên ngành theo tên ngành """
        return [nganh for nganh in self.get_all_nganh_hoc() if nganh.ten_nganh == ten_nganh]

    def find_index_nganh_hoc(self, chuyen_nganh):
        """ Tìm vị trí của chuyên ngành trong danh sách """
        return next((i for i, nganh in enumerate(self.get_all_nganh_hoc()) if nganh.chuyen_nganh == chuyen_nganh), -1)

    def save_new_nganh_hoc(self, nganh):
        """ Lưu chuyên ngành mới vào danh sách """
        all_nganh_hoc = self.get_all_nganh_hoc()
        all_nganh_hoc.append(nganh)
        self.json_factory.write_data(all_nganh_hoc, self.file_nganh_hoc)

    def save_update_nganh_hoc(self, updated_nganh):
        """ Cập nhật thông tin chuyên ngành """
        all_nganh_hoc = self.get_all_nganh_hoc()
        index = self.find_index_nganh_hoc(updated_nganh.chuyen_nganh)
        if index != -1:
            all_nganh_hoc[index] = updated_nganh
            self.json_factory.write_data(all_nganh_hoc, self.file_nganh_hoc)

    def delete_nganh_hoc(self, chuyen_nganh):
        """ Xóa chuyên ngành khỏi danh sách """
        all_nganh_hoc = self.get_all_nganh_hoc()
        index = self.find_index_nganh_hoc(chuyen_nganh)
        if index != -1:
            all_nganh_hoc.pop(index)
            self.json_factory.write_data(all_nganh_hoc, self.file_nganh_hoc)

    def save_new_khach(self, khach):
        """ Lưu thông tin khách mới vào file JSON """
        all_khach = self.get_all_khach()
        khach.ma_nguoi_dung = self.get_next_khach_id()
        all_khach.append(khach)
        self.json_factory.write_data(all_khach, self.file_khach)

    def get_next_khach_id(self):
        """Lấy ID khách tiếp theo dưới dạng 'K + số thứ tự'"""
        all_khach = self.get_all_khach()
        if not all_khach:
            return "K1"
        max_id = max(int(khach.ma_nguoi_dung[1:]) for khach in all_khach if khach.ma_nguoi_dung.startswith("K"))
        return f"K{max_id + 1}"

    def save_nganh_hoc_to_json(self, data):
        """Ghi đè danh sách ngành học vào file JSON"""
        with open(self.file_nganh_hoc, "w", encoding="utf-8") as file:
            json.dump([nganh.to_dict() for nganh in data], file, ensure_ascii=False, indent=4)

    def load_nganh_hoc_from_json(self):
        """Đọc danh sách ngành học từ file JSON"""
        try:
            with open(self.file_nganh_hoc, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Nganh_hoc.from_dict(nganh) for nganh in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
