# bai3
def tim_so_lon_nhat(a, b, c):
    # tim so lon nhat
    return max(a, b, c)
# nhap so
so1 = float(input("nhap so thu 1: "))
so2 = float(input("nhap so thu 2: "))
so3 = float(input("nhap so thu 3: "))
# tim so lon nhat
so_lon_nhat = tim_so_lon_nhat(so1, so2, so3)
# in ra ket qua
print(f"so lon nhat trong 3 so la: {so_lon_nhat}")
