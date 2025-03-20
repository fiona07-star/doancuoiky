from Spydecat_K24406H.libs.JsonFileFactory import JsonFileFactory
from Spydecat_K24406H.models.Nganh_hoc import Nganh_hoc

nganh_hoc=[]
jff=JsonFileFactory()
filename="../dataset/nganh_hoc.json"
nganh_hoc=jff.read_data(filename,Nganh_hoc)
print("Danh sách ngành:")
for nganh in nganh_hoc:
    print(nganh)