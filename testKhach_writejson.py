from Spydecat_K24406H.libs.JsonFileFactory import JsonFileFactory
from Spydecat_K24406H.models.Khach import Khach

khach=[]
khach.append(Khach('K1', 'Võ Quốc Anh', 'qav@gmail.com', '0362877656', True,2006))
khach.append(Khach('K2', 'Nguyễn Thị Thảo', 'thao@gmail.com', '0987887632', False,2007))
khach.append(Khach('K3', 'Trần Mạnh', 'manhtran@gmail.com', '0372655231', True,1999))
khach.append(Khach('K4', 'Trần Thị Hoa', 'hoa@gmail.com', '0274588653', False, 2004))
khach.append(Khach('K5', 'Nguyễn Trung Hiếu', 'hieutrung@gmail.com', '0986321875', True,2007))
print("Danh sách khách xem:")
for k in khach:
    print(k)
jff=JsonFileFactory()
filename="../dataset/khach.json"
jff.write_data(khach,filename)