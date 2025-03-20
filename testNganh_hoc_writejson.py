from Spydecat_K24406H.libs.JsonFileFactory import JsonFileFactory
from Spydecat_K24406H.models.Nganh_hoc import Nganh_hoc

nganh_hoc=[]
nganh_hoc.append(Nganh_hoc('Kinh tế', 'Chuyên ngành Kinh tế học', '7310101_401', 60,'24,6', '80', '847','25,89'))
nganh_hoc.append(Nganh_hoc('Marketing', 'Chuyên ngành Digital Marketing', '7310101_417', 60,'26', '82', '897','26,89'))
nganh_hoc.append(Nganh_hoc('Luật', 'Chuyên ngành Luật Dân sự', '7310101_503', 60,'25,6', '84', '927','25,97'))
nganh_hoc.append(Nganh_hoc('Luật kinh tế', 'Chuyên ngành Luật Kinh doanh', '7310101_501', 60,'26,6', '80,7', '807','26,4'))
nganh_hoc.append(Nganh_hoc('Hệ thống thông tin quản lý', 'Chuyên ngành Kinh doanh số và Trí tuệ nhân tạo', '7310101_416', 60,'27,6', '86,3', '942','25,89'))
nganh_hoc.append(Nganh_hoc('Kinh tế', 'Chuyên ngành Kinh tế chính tri', '7310101_401', 60,'24,6', '80', '847','25,89'))
nganh_hoc.append(Nganh_hoc('Kinh tế', 'Chuyên ngành Kinh tế quốc tế', '7310101_401', 60,'24,6', '80', '847','25,89'))
nganh_hoc.append(Nganh_hoc('Marketing', 'Chuyên ngành Marketing', '7310101_417', 60,'26', '82', '897','26,89'))
nganh_hoc.append(Nganh_hoc('Luật kinh tế', 'Chuyên ngành Luật Thương mại quốc tế', '7310101_501', 60,'26,6', '80,7', '807','26,4'))
nganh_hoc.append(Nganh_hoc('Hệ thống thông tin quản lý', 'Chuyên ngành hệ thống thông tin quản lý', '7310101_416', 60,'27,6', '86,3', '942','25,89'))

print("Danh sách ngành:")
for nganh in nganh_hoc:
    print(nganh)
jff=JsonFileFactory()
filename="../dataset/nganh_hoc.json"
jff.write_data(nganh_hoc,filename)