#bài 2
# nhập x 
x = float(input("nhap gia tri cua x: "))
# phép tính
tu_so = -x + (x**2 + 4)**(1/2) 
mau_so = (x**4 + 1)**(1.7)
f_x = tu_so/mau_so
#tính
ket_qua = round(f_x, 2)
#in kết quả
print("gia tri cua bieu thuc la :",ket_qua)