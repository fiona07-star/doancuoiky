class NguoiDung:
    def __init__(self,ma_nguoi_dung,ten,email):
        self.ma_nguoi_dung=ma_nguoi_dung
        self.ten=ten
        self.email=email
    def __str__(self):
        return f"{self.ma_nguoi_dung}\t{self.ten}\t{self.email}"