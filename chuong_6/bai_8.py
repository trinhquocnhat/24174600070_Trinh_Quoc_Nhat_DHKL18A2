#bài 8
# nhap x 
x = float(input("nhap gia tri x:"))
# phép tính
log_4_x = math.log(x, 4)
log_x_2 = math.log(2, x)
# tính toán
dap_an = log_4_x + log_x_2
dap_an = round(dap_an, 2)
# kết quả 
print("gia tri cua bieu thuc la: ", dap_an)