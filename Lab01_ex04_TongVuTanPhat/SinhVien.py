class SinhVien:
    def __init__(self, id, hoTen, ngaySinh, diemTB, sex, major):
        self.id = id
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh
        self.diemTB = diemTB
        self.sex = sex
        self.major = major
        self._hocLuc = ""

    def toString(self):
        return f"ID: {self.id}, Họ tên: {self.hoTen}, Ngày sinh: {self.ngaySinh}, Điểm TB: {self.diemTB}, Giới tính: {self.sex}, Chuyên ngành: {self.major}, Học lực: {self._hocLuc}"