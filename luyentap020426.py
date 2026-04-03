# ===============================
# 1. Hàm tính tổng 2 số
# ===============================
def tong_2_so(a, b):
    return a + b


# ===============================
# 2. Hàm tính tổng các số truyền vào
# ===============================
def tong_n_so(*args):
    return sum(args)


# ===============================
# 3. Hàm kiểm tra số nguyên tố
# ===============================
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# ===============================
# 4. Tìm số nguyên tố trong [a,b]
# ===============================
def tim_so_nguyen_to(a, b):
    ds = []
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            ds.append(i)
    return ds


# ===============================
# 5. Hàm kiểm tra số hoàn hảo
# ===============================
def la_so_hoan_hao(n):
    if n <= 0:
        return False

    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i

    return tong == n


# ===============================
# 6. Tìm số hoàn hảo trong [a,b]
# ===============================
def tim_so_hoan_hao(a, b):
    ds = []
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            ds.append(i)
    return ds


# ===============================
# 7. MENU CHƯƠNG TRÌNH
# ===============================
def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Tính tổng 2 số")
        print("2. Tính tổng nhiều số")
        print("3. Kiểm tra số nguyên tố")
        print("4. Tìm số nguyên tố trong [a,b]")
        print("5. Kiểm tra số hoàn hảo")
        print("6. Tìm số hoàn hảo trong [a,b]")
        print("0. Thoát")

        chon = int(input("Nhập lựa chọn: "))

        if chon == 1:
            a = int(input("a = "))
            b = int(input("b = "))
            print("Tổng =", tong_2_so(a, b))

        elif chon == 2:
            ds = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split()))
            print("Tổng =", tong_n_so(*ds))

        elif chon == 3:
            n = int(input("Nhập n: "))
            if la_so_nguyen_to(n):
                print("Là số nguyên tố")
            else:
                print("Không phải số nguyên tố")

        elif chon == 4:
            a = int(input("a = "))
            b = int(input("b = "))
            print("Các số nguyên tố:", tim_so_nguyen_to(a, b))

        elif chon == 5:
            n = int(input("Nhập n: "))
            if la_so_hoan_hao(n):
                print("Là số hoàn hảo")
            else:
                print("Không phải số hoàn hảo")

        elif chon == 6:
            a = int(input("a = "))
            b = int(input("b = "))
            print("Các số hoàn hảo:", tim_so_hoan_hao(a, b))

        elif chon == 0:
            print("Thoát chương trình!")
            break

        else:
            print("Chọn sai!")


# ===============================
# CHẠY CHƯƠNG TRÌNH
# ===============================
menu()