#bai9
def tinh_cuoc_taxi(loai_xe, quang_duong, thoi_gian_cho):
    # cuoc phi xe
    cuoc_phi = 0
 # cuoc theo loai xe
    if loai_xe == 4:
        if quang_duong <= 0.8:
            cuoc_phi = 11000
        elif quang_duong <= 20:
            cuoc_phi = 11000 + (quang_duong - 0.8) * 12100
        else:
            cuoc_phi = 11000 + 19.2 * 12100 + (quang_duong - 20) * 10000
    elif loai_xe == 7:
        if quang_duong <= 0.8:
            cuoc_phi = 13000
        elif quang_duong <= 30:
            cuoc_phi = 13000 + (quang_duong - 0.8) * 14100
        else:
            cuoc_phi = 13000 + 29.2 * 14100 + (quang_duong - 30) * 12000
    else:
        return "loai xe khong hop le chi 4 cho hoac 7 cho."
 #thoi gian xe cho
    if thoi_gian_cho > 5:
        cuoc_phi += (thoi_gian_cho - 5) * 800
    return cuoc_phi
# thong tin nguoi dung xe
loai_xe = int(input("nhap loai xe (4 cho hoac 7 cho): "))
quang_duong = float(input("nhap quang duong di (km): "))
thoi_gian_cho = int(input("nhap thoi gian cho (phut): "))
# Tinh
cuoc_phi = tinh_cuoc_taxi(loai_xe, quang_duong, thoi_gian_cho)
#in ra ket qua
print(f"cuoc phi phai tra: {cuoc_phi} dong")
