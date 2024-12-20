
# Danh sách mặt hàng
danh_sach_mat_hang = []


def tinh_thanh_tien(don_gia, so_luong):
    return don_gia * so_luong


def tinh_vat(thanh_tien):
    return thanh_tien * 0.1


def xem_danh_sach():
    print("\nDanh sách mặt hàng:")
    for mh in danh_sach_mat_hang:
        print(f"Mã: {mh['ma_hang']}, Tên: {mh['ten_hang']}, Đơn vị: {mh['don_vi_tinh']}, Đơn giá: {mh['don_gia']}, "
              f"Số lượng: {mh['so_luong']}, Thành tiền: {mh['thanh_tien']}, Thuế VAT: {mh['vat']}")


def nhap_mat_hang():
    ma_hang = input("Nhập mã mặt hàng: ")
    ten_hang = input("Nhập tên mặt hàng: ")
    don_vi_tinh = input("Nhập đơn vị tính: ")
    don_gia = float(input("Nhập đơn giá: "))
    so_luong = int(input("Nhập số lượng: "))
    thanh_tien = tinh_thanh_tien(don_gia, so_luong)
    vat = tinh_vat(thanh_tien)
    mat_hang = {
        'ma_hang': ma_hang,
        'ten_hang': ten_hang,
        'don_vi_tinh': don_vi_tinh,
        'don_gia': don_gia,
        'so_luong': so_luong,
        'thanh_tien': thanh_tien,
        'vat': vat
    }
    danh_sach_mat_hang.append(mat_hang)
    print("Thêm mặt hàng thành công!")


def tim_kiem_mat_hang():
    ma_hang = input("Nhập mã mặt hàng cần tìm: ")
    for mh in danh_sach_mat_hang:
        if mh['ma_hang'] == ma_hang:
            print(f"Tìm thấy mặt hàng: {mh['ten_hang']}")
            return mh
    print("Không tìm thấy mặt hàng!")
    return None


def xoa_mat_hang():
    mat_hang = tim_kiem_mat_hang()
    if mat_hang:
        danh_sach_mat_hang.remove(mat_hang)
        print("Xóa mặt hàng thành công!")


def chinh_sua_mat_hang():
    mat_hang = tim_kiem_mat_hang()
    if mat_hang:
        mat_hang['ten_hang'] = input("Nhập tên mới: ")
        mat_hang['don_vi_tinh'] = input("Nhập đơn vị tính mới: ")
        mat_hang['don_gia'] = float(input("Nhập đơn giá mới: "))
        mat_hang['so_luong'] = int(input("Nhập số lượng mới: "))
        mat_hang['thanh_tien'] = tinh_thanh_tien(mat_hang['don_gia'], mat_hang['so_luong'])
        mat_hang['vat'] = tinh_vat(mat_hang['thanh_tien'])
        print("Chỉnh sửa thành công!")


def sap_xep_theo_ten():
    danh_sach_mat_hang.sort(key=lambda x: x['ten_hang'])
    print("Danh sách đã được sắp xếp theo tên mặt hàng!")


# Menu
while True:
    print("\nChương trình quản lý hàng hóa:")
    print("1. Xem danh sách mặt hàng")
    print("2. Nhập thông tin mặt hàng")
    print("3. Tìm kiếm và chỉnh sửa thông tin mặt hàng")
    print("4. Tìm kiếm và xóa mặt hàng")
    print("5. Xem danh sách mặt hàng sắp xếp theo tên mặt hàng")
    print("6. Thoát chương trình")
    lua_chon = int(input("Nhập lựa chọn: "))

    if lua_chon == 1:
        xem_danh_sach()
    elif lua_chon == 2:
        nhap_mat_hang()
    elif lua_chon == 3:
        chinh_sua_mat_hang()
    elif lua_chon == 4:
        xoa_mat_hang()
    elif lua_chon == 5:
        sap_xep_theo_ten()
        xem_danh_sach()
    elif lua_chon == 6:
        print("Thoát chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ!")