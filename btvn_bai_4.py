# bai4
def kiem_tra_tam_giac(a, b, c):
    # kiem tra dieu kien tam giac
    if a + b > c and a + c > b and b + c > a:
        #kiem tra loai tam giac
        if a == b == c:
            return "tam giac deu"
        elif a == b or a == c or b == c:
            if(a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
                return "tam giac vuong can"
            return " tam giac can"
        elif (a**2 + b**2 == c**2) or  (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            return "tam giac vuong"
        else:
            return "tam giac thuong"
    else:
        return "khong phai la bo ba cua canh tam giac"
    #nhap cac canh a, b, c
a = float(input("nhap canh a: "))
b = float(input("nhap canh b: "))
c = float(input("nhap canh c: "))
#goi ham
result = kiem_tra_tam_giac(a, b, c)
#in ket qua
print(result)