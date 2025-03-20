from Spydecat_K24406H.libs.JsonFileFactory import JsonFileFactory
from Spydecat_K24406H.models.CBNV import Canbo

cbnvs=[]
jff=JsonFileFactory()
filename="../dataset/cbnv.json"
cbnvs=jff.read_data(filename,Canbo)
print("Danh sách cán bộ nhân viên:")
for cbnv in cbnvs:
    print(cbnv)