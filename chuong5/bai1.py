import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = "d:/python/chuong5/data.txt"

n = int(input("Nhập số dòng cần đọc: "))

try:
    with open(file_path, "r", encoding="utf-8") as f:
        i = 0
        while i < n:
            line = f.readline()
            if not line:
                break
            print(line.strip())
            i += 1

except FileNotFoundError:
    print("❌ Không tìm thấy file data.txt!")