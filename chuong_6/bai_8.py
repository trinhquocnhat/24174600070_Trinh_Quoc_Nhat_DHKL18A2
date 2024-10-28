# Hàm tính điểm trung bình và xếp loại
def xep_loai_diem(diem_chuyen_can, diem_giua_ky, diem_cuoi_ky):
    # Tính điểm trung bình
    diem_trung_binh = (diem_chuyen_can + diem_giua_ky + diem_cuoi_ky) / 3

    # Xếp loại
    if diem_trung_binh >= 9:
        loai = 'A'
    elif diem_trung_binh >= 7:
        loai = 'B'
    elif diem_trung_binh >= 5:
        loai = 'C'
    else:
        loai = 'D'
    return diem_trung_binh, loa
# Nhập điểm từ người dùng
diem_chuyen_can = float(input("Nhập điểm chuyên cần: "))
diem_giua_ky = float(input("Nhập điểm giữa kỳ: "))
diem_cuoi_ky = float(input("Nhập điểm cuối kỳ: "))

# Gọi hàm và in kết quả
diem_trung_binh, loai = xep_loai_diem(diem_chuyen_can, diem_giua_ky, diem_cuoi_ky)
print(f"Điểm trung bình: {diem_trung_binh:.2f}")
print(f"Xếp loại: {loai}")