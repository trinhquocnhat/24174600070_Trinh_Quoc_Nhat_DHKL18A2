# bai2
import math 
def la_diem_trong_hoac_ngoai_hinh_tron(x, y, a, b, r):
    # khoang cach tu diem M den tam I
    khoang_cach_cua_binh_phuong = (x - a) ** 2 + (y - b) ** 2
    # so sanh voi ban kinh binh phuong
    return khoang_cach_cua_binh_phuong <= r ** 2
# nhap toa do
x = float(input("nhap toa do x cua diem M: "))
y = float(input("nhap toa do y cua diem M: "))
a = float(input("nhap toa do x cua tam I: "))
b = float(input("nhap toa do y cua tam I: "))
r = float(input("nhap ban kinh r cua hinh tron: "))
# kiem tra
result = la_diem_trong_hoac_ngoai_hinh_tron(x, y, a, b, r)
# in ra ket qua
print(result)  
