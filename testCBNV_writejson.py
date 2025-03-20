from Spydecat_K24406H.libs.JsonFileFactory import JsonFileFactory
from Spydecat_K24406H.models.CBNV import Canbo

cbnvs=[]
cbnvs.append(Canbo('C1', 'Au Tu Ngoc', 'atn@gmail.com', '123', 'Phòng CTSV'))
cbnvs.append(Canbo('C2', 'Tran Khanh Ly', 'tkl@gmail.com', '234', 'Phòng CTSV'))
cbnvs.append(Canbo('C3', 'Nguyen Nhu Quynh', 'nnq@gmail.com', '345', 'Phòng CTSV'))

print("Danh sách CBNV:")
for cbnv in cbnvs:
    print(cbnv)
jff=JsonFileFactory()
filename="../dataset/cbnv.json"
jff.write_data(cbnvs,filename)