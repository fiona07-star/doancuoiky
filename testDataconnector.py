from Spydecat_K24406H.libs.Dataconnector import DataConnector
from Spydecat_K24406H.models.Khach import Khach
from Spydecat_K24406H.models.Nganh_hoc import Nganh_hoc

dc = DataConnector()

# Test lấy danh sách khách
print("=== Danh sách khách ===")
khach = dc.get_all_khach()
for k in khach:
    print(k)

# Test lấy danh sách CBNV
print("\n=== Danh sách CBNV ===")
cbnvs = dc.get_all_cbnv()
for cbnv in cbnvs:
    print(cbnv)

# Test lấy danh sách ngành học
print("\n=== Danh sách ngành học ===")
nganh_hoc = dc.get_all_nganh_hoc()
for nganh in nganh_hoc:
    print(nganh)

# Test đăng nhập
print("\n=== Kiểm tra đăng nhập ===")
uid = "teo"  # đổi uid và pwd cho khớp dữ liệu thật trong cbnv.json của bạn
pwd = "123hhgđghjk"
emp = dc.login(uid, pwd)
if emp is not None:
    print("Đăng nhập thành công:", emp)
else:
    print("Đăng nhập thất bại")

# Test thêm khách mới
print("\n=== Thêm khách mới ===")
new_khach = Khach(
    ma_nguoi_dung="",  # để trống vì DataConnector sẽ gán tự động
    ten="Trần Thị B",
    email="tranthib@example.com",
    sdt="0988111222",
    gioi_tinh=False,
    nam_sinh=1998
)
dc.save_new_khach(new_khach)
print("Danh sách khách sau khi thêm:")
for k in dc.get_all_khach():
    print(k)

# Test thêm ngành học mới
print("\n=== Thêm ngành học mới ===")
new_nganh = Nganh_hoc(
    ten_nganh="Quản trị kinh doanh",
    chuyen_nganh="Marketing",
    ma_tuyen_sinh="7340101",
    chi_tieu=150,
    phuong_thuc_1a=50,
    phuong_thuc_1b=30,
    phuong_thuc_2=40,
    phuong_thuc_3=30
)
dc.save_new_nganh_hoc(new_nganh)
print("Danh sách ngành học sau khi thêm:")
for nganh in dc.get_all_nganh_hoc():
    print(nganh)

# Test cập nhật ngành học
print("\n=== Cập nhật ngành học ===")
updated_nganh = Nganh_hoc(
    ten_nganh="Quản trị kinh doanh",
    chuyen_nganh="Marketing",
    ma_tuyen_sinh="7340101",
    chi_tieu=180,
    phuong_thuc_1a=60,
    phuong_thuc_1b=40,
    phuong_thuc_2=50,
    phuong_thuc_3=30
)
dc.save_update_nganh_hoc(updated_nganh)
print("Danh sách ngành học sau khi cập nhật:")
for nganh in dc.get_all_nganh_hoc():
    print(nganh)

# Test xoá ngành học
print("\n=== Xoá ngành học ===")
dc.delete_nganh_hoc("Marketing")
print("Danh sách ngành học sau khi xoá:")
for nganh in dc.get_all_nganh_hoc():
    print(nganh)