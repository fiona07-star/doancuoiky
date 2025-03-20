from Spydecat_K24406H.models.User import NguoiDung


class Khach(NguoiDung):
    def __init__(self, ma_nguoi_dung, ten, email, sdt, gioi_tinh, nam_sinh):
        super().__init__(ma_nguoi_dung, ten, email)
        self.sdt = sdt
        self.nam_sinh = nam_sinh

        # Chuẩn hóa giới tính: nhận True/False hoặc "Nam"/"Nữ"
        if isinstance(gioi_tinh, str):
            self.gioi_tinh = True if gioi_tinh.strip().lower() == "nam" else False
        else:
            self.gioi_tinh = gioi_tinh

    def __str__(self):
        msg = super().__str__()
        gioi_tinh_text = "Nam" if self.gioi_tinh else "Nữ"
        return f"{msg}\t{self.sdt}\t{gioi_tinh_text}\t{self.nam_sinh}"