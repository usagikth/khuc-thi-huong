class HocVien:
    # a) Tạo class hoc_vien với các thuộc tính tương ứng
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    # b) Tạo phương thức show_info trả về đầy đủ thông tin của học viên
    def show_info(self):
        info = (f"Họ tên: {self.ho_ten}\n"
                f"Ngày sinh: {self.ngay_sinh}\n"
                f"Email: {self.email}\n"
                f"Điện thoại: {self.dien_thoai}\n"
                f"Địa chỉ: {self.dia_chi}\n"
                f"Lớp: {self.lop}")
        return info

    # c) Tạo phương thức change_info thay đổi thông tin với tham số mặc định
    def change_info(self, dia_chi="Hà Nội", lop="IT12.x"):
        self.dia_chi = dia_chi
        self.lop = lop
        print(f"--- Đã cập nhật thông tin cho học viên {self.ho_ten} ---")

# d) Chương trình chính
if __name__ == "__main__":
    # Tạo đối tượng thuộc lớp HocVien
    hoc_vien_1 = HocVien(
        ho_ten="Nguyễn Văn Huỳnh",
        ngay_sinh="01/01/2000",
        email="vana@email.com",
        dien_thoai="0123456789",
        dia_chi="Hai Phong",
        lop="IT10.a"
    )

    # Gọi phương thức show_info để xem thông tin ban đầu
    print("Thông tin ban đầu:")
    print(hoc_vien_1.show_info())
    print("-" * 30)

    # Gọi phương thức change_info sử dụng các tham số mặc định
    hoc_vien_1.change_info()

    # Gọi lại show_info để kiểm tra thay đổi
    print("Thông tin sau khi thay đổi:")
    print(hoc_vien_1.show_info())