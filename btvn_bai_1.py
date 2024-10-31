# bai1
def nam_nhuan(year):
    # nam nhuan chia het cho 4 va khong chia het cho 100
    # chia het cho 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
# nam
year = int(input("nhap nam: "))
if nam_nhuan(year):
    print(f"nam {year} nam nhuan.")
else:
    print(f"nam {year} khong phai nam nhuan.")