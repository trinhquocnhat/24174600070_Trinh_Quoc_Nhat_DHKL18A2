#bai 8
# phan loai sinh vien dua tren diem
def phan_loai_sinh_vien(diem_hoc_tap):
    if diem_hoc_tap == 'A':
        return "sinh vien loai xuat sac"
    elif diem_hoc_tap == 'B':
        return "sinh vien loai gioi"
    elif diem_hoc_tap == 'C':
        return "sinh vien loai kha"
    elif diem_hoc_tap == 'D':
        return "sinh vien loai trung binh"
    elif diem_hoc_tap == 'E':
        return "sinh vien loai yeu"
    elif diem_hoc_tap == 'F':
        return "sinh vien loai kem"
    else:
        return "diem khong chinh xac"
# nhap diem
diem_sinh_vien = input("nhap diem sinh vien (A, B, C, D, E, F): ")
ket_qua = phan_loai_sinh_vien(diem_sinh_vien)
#in ra ket qua
print("ket qua:", ket_qua)