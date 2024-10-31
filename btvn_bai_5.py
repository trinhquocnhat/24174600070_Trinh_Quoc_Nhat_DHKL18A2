#bai5
# nhap ki tu tu ban phim
ky_tu = input("nhap 1 ki tu: ").lower()
# kiem tra xem la phu am hay nguyen am
if ky_tu in 'aeiou':
    print(f"{ky_tu} la nguyen am")
elif ky_tu.isalpha():
    print(f"{ky_tu} la phu am")
else:
    print(f"{ky_tu} khong phai la ky tu trong bang chu cai tieng anh")