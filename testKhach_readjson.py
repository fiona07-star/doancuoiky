from Spydecat_K24406H.libs.JsonFileFactory import JsonFileFactory
from Spydecat_K24406H.models.Khach import Khach

khach=[]
jff=JsonFileFactory()
filename="../dataset/khach.json"
khach=jff.read_data(filename,Khach)
print("Danh sách khách xem:")
for k in khach:
    print(k)