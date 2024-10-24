#bai 1
import math
    # Nhập bán kính và chiều cao từ bàn phím
r  = float(input("Nhập bán kính (r): "))
h  = float(input("Nhập chiều cao (h): "))
pi = 3.14
       #Tính diện tích xung quanh, diện tích toàn phần và thể tích khối trụ
S_xung_quanh = 2 * math.pi * r * h
S_toan_phan = 2 * math.pi * r * h + 2 * pi * r**2
the_tich = pi * r**2 * h
# Kết quả
print(f"Diện tích xung quanh: {round(S_xung_quanh, 2)} ")
print(f"Diện tích toàn phần: {round(S_toan_phan, 2)} ")
print(f"Thể tích: {round(the_tich, 2)}")
