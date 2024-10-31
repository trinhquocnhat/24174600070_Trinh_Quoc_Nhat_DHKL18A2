#bai06
def menu():
    print("rap chieu phim ABC")
    print("1.phim tinh cam")
    print("2. phim kinh di")
    print("3. phim hoat hinh")
    print("4. phim khoa hoc vien tuong")
    def lua_chon():
        menu()
        chon = input("nhap so phim ban muon xem: ")
        if chon == '1':
            print("chon the loai phim tinh cam.")
        elif chon == '2' :
            print("chon the loai phim kinh di")
        elif chon == '3' :
            print("chon the loai phim hoat hinh")
        elif chon == '4' :
            print("chon the loai phim khoa hoc vien tuong")
            return 
        else:
          print("lua chon khong hop le vui long chon lai")
#goi ham
result = menu()
#in ra ket qua
print(result)