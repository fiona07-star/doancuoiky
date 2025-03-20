class Nganh_hoc:
    def __init__(self, ten_nganh, chuyen_nganh, ma_tuyen_sinh, chi_tieu, phuong_thuc_1a, phuong_thuc_1b, phuong_thuc_2, phuong_thuc_3):
        self.ten_nganh = ten_nganh
        self.chuyen_nganh = chuyen_nganh
        self.ma_tuyen_sinh = ma_tuyen_sinh
        self.chi_tieu = chi_tieu
        self.phuong_thuc_1a = phuong_thuc_1a
        self.phuong_thuc_1b = phuong_thuc_1b
        self.phuong_thuc_2 = phuong_thuc_2
        self.phuong_thuc_3 = phuong_thuc_3

    def __str__(self):
        return f"{self.ten_nganh}\t{self.chuyen_nganh}\t{self.ma_tuyen_sinh}\t{self.chi_tieu}\t{self.phuong_thuc_1a}\t{self.phuong_thuc_1b}\t{self.phuong_thuc_2}\t{self.phuong_thuc_3}"

    def to_dict(self):
        """Chuyển đối tượng thành dictionary để lưu JSON"""
        return {
            "ten_nganh": self.ten_nganh,
            "chuyen_nganh": self.chuyen_nganh,
            "ma_tuyen_sinh": self.ma_tuyen_sinh,
            "chi_tieu": self.chi_tieu,
            "phuong_thuc_1a": self.phuong_thuc_1a,
            "phuong_thuc_1b": self.phuong_thuc_1b,
            "phuong_thuc_2": self.phuong_thuc_2,
            "phuong_thuc_3": self.phuong_thuc_3
        }

    @classmethod
    def from_dict(cls, data):
        """Khởi tạo đối tượng từ dictionary (dùng khi đọc từ JSON)"""
        return cls(
            data["ten_nganh"], data["chuyen_nganh"], data["ma_tuyen_sinh"],
            data["chi_tieu"], data["phuong_thuc_1a"], data["phuong_thuc_1b"],
            data["phuong_thuc_2"], data["phuong_thuc_3"]
        )
