#bai7
import math
# Chuong trinh giai he phuong trinh bac nhat 2 an
def giai_he_phuong_trinh():
    # Nhap cac he so
    a1 = float(input("Nhap a1: "))
    b1 = float(input("Nhap b1: "))
    c1 = float(input("Nhap c1: "))
    a2 = float(input("Nhap a2: "))
    b2 = float(input("Nhap b2: "))
    c2 = float(input("Nhap c2: "))
     # Tinh dinh thuc
    D = a1 * b2 - a2 * b1 
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1  
    # Xet cac truong hop
    if D == 0:
        if Dx == 0 and Dy == 0:
            print("He phuong trinh co vo so nghiem")
        else:
            print("He phuong trinh vo nghiem")
    else:
        x = Dx / D
        y = Dy / D
        print("Nghiem cua phuong trinh la: ")
        print("x =", x)
        print("y =", y)
# Goi ham
giai_he_phuong_trinh()