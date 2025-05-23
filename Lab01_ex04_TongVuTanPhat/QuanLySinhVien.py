from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        maxID = 1
        if self.listSinhVien:
            for sv in self.listSinhVien:
                if maxID <= sv.id:
                    maxID = sv.id
            maxID += 1
        return maxID

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svID = self.generateID()
        hoTen = input("Nhập họ tên: ")
        ngaySinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
        diemTB = float(input("Nhập điểm trung bình: "))
        sex = input("Nhập giới tính: ")
        major = input("Nhập chuyên ngành: ")
        sv = SinhVien(svID, hoTen, ngaySinh, diemTB, sex, major)
        self.xeploaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findById(ID)
        if sv is not None:
            print("\nNhập thông tin mới cho sinh viên:")
            sv.hoTen = input("Nhập họ tên: ")
            sv.ngaySinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
            sv.diemTB = float(input("Nhập điểm trung bình: "))
            sv.sex = input("Nhập giới tính: ")
            sv.major = input("Nhập chuyên ngành: ")
            self.xeploaiHocLuc(sv)
            print("\nCập nhật thông tin sinh viên thành công!")
        else:
            print("\nSinh viên có ID =", ID, "không tồn tại.")

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x.id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x.hoTen, reverse=False)

    def sortByDiemTb(self):
        self.listSinhVien.sort(key=lambda x: x.diemTB, reverse=True)

    def findById(self, ID):
        for sv in self.listSinhVien:
            if sv.id == ID:
                return sv
        return None

    def findByName(self, keyword):
        listSV = []
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if keyword.lower() in sv.hoTen.lower():
                    listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        sv = self.findById(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)
            return True
        return False

    def xeploaiHocLuc(self, sv):
        if sv.diemTB >= 8:
            sv._hocLuc = "Giỏi"
        elif sv.diemTB >= 6.5:
            sv._hocLuc = "Khá"
        elif sv.diemTB >= 5:
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"

    def showSinhVien(self, listSV):
        if not listSV:
            print("Danh sách trống!")
            return
        for sv in listSV:
            print(sv.toString())

    def getListSinhVien(self):
        return self.listSinhVien