from Spydecat_K24406H.models.User import NguoiDung


class Canbo(NguoiDung):
    def __init__(self, ma_nguoi_dung, ten, email, mat_khau, phong_ban):
        super().__init__(ma_nguoi_dung, ten, email)
        self.mat_khau = mat_khau
        self.phong_ban = phong_ban

    def __str__(self):
        msg = super().__str__()
        return f"{msg}\t{self.mat_khau}\t{self.phong_ban}"