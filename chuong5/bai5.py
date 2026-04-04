import os

# Lấy đường dẫn file
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "demo_file2.txt")

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

        # Tách từ
        words = content.split()

        # Đếm số lần xuất hiện
        dem = {}

        for word in words:
            if word in dem:
                dem[word] += 1
            else:
                dem[word] = 1

        print(dem)

except FileNotFoundError:
    print("❌ Không tìm thấy file demo_file2.txt")