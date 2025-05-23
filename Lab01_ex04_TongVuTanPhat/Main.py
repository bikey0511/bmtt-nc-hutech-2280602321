from QuanLySinhVien import QuanLySinhVien

if __name__ == "__main__":
    qlsv = QuanLySinhVien()

    while True:
        print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
        print("************************MENU************************")
        print("1. Thêm sinh viên")
        print("2. Cập nhật thông tin sinh viên theo ID")
        print("3. Xóa sinh viên theo ID")
        print("4. Tìm kiếm sinh viên theo tên")
        print("5. Sắp xếp sinh viên theo ID")
        print("6. Sắp xếp sinh viên theo tên")
        print("7. Sắp xếp sinh viên theo điểm trung bình")
        print("8. Hiển thị danh sách sinh viên")
        print("0. Thoát chương trình")
        key = int(input("Nhập lựa chọn: "))

        if key == 1:
            print("\n1. Thêm sinh viên")
            qlsv.nhapSinhVien()
            print("\nThêm sinh viên thành công!")
        elif key == 2:
            if qlsv.soLuongSinhVien() > 0:
                print("\n2. Cập nhật thông tin sinh viên")
                ID = int(input("Nhập ID: "))
                qlsv.updateSinhVien(ID)
            else:
                print("\nDanh sách sinh viên trống!")
        elif key == 3:
            if qlsv.soLuongSinhVien() > 0:
                print("\n3. Xóa sinh viên")
                ID = int(input("Nhập ID: "))
                if qlsv.deleteById(ID):
                    print("\nSinh viên có ID =", ID, "đã bị xóa.")
                else:
                    print("\nSinh viên có ID =", ID, "không tồn tại.")
            else:
                print("\nDanh sách sinh viên trống!")
        elif key == 4:
            if qlsv.soLuongSinhVien() > 0:
                print("\n4. Tìm kiếm sinh viên theo tên")
                keyword = input("Nhập tên để tìm kiếm: ")
                searchResult = qlsv.findByName(keyword)
                qlsv.showSinhVien(searchResult)
            else:
                print("\nDanh sách sinh viên trống!")
        elif key == 5:
            if qlsv.soLuongSinhVien() > 0:
                print("\n5. Sắp xếp sinh viên theo ID")
                qlsv.sortByID()
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("\nDanh sách sinh viên trống!")
        elif key == 6:
            if qlsv.soLuongSinhVien() > 0:
                print("\n6. Sắp xếp sinh viên theo tên")
                qlsv.sortByName()
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("\nDanh sách sinh viên trống!")
        elif key == 7:
            if qlsv.soLuongSinhVien() > 0:
                print("\n7. Sắp xếp sinh viên theo điểm trung bình")
                qlsv.sortByDiemTb()
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("\nDanh sách sinh viên trống!")
        elif key == 8:
            if qlsv.soLuongSinhVien() > 0:
                print("\n8. Hiển thị danh sách sinh viên")
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("\nDanh sách sinh viên trống!")
        elif key == 0:
            print("\nBạn đã chọn thoát chương trình!")
            break
        else:
            print("\nKhông có chức năng này!")
            print("\nHãy chọn chức năng trong hộp menu.")