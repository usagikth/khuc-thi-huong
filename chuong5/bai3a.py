import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "demo_file1.txt")

try:
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())

except FileNotFoundError:
    print("❌ Không tìm thấy file demo_file1.txt")