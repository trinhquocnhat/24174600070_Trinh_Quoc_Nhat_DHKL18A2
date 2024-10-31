#bai10
def tinh_thue_thu_nhap(luong):
    #thue dua tren muc luong
    if luong >= 15000000:
        thue = luong * 0.3
    elif 7000000 <= luong < 15000000:
        thue = luong * 0.2
    else:
        thue = luong * 0.1
    return thue
def tinh_luong_rong(luong):
    #luong rong sau khi tru thue
    thue = tinh_thue_thu_nhap(luong)
    luong_rong = luong - thue
    return luong_rong
# nhap muc long nhan vien
luong = float(input("nhap muc luong nhan vien (vnd): "))
# tinh thue va luong rong
thue = tinh_thue_thu_nhap(luong)
luong_rong = tinh_luong_rong(luong)
# in ra ket qua
print(f"thue thu nhap phai tra: {thue} vnd")
print(f"luong rong tra cho nan vien: {luong_rong} vnd")