# Nhập thông tin
ten = input("Tên: ")
tuoi = input("Tuổi: ")
email = input("Email: ")
skype = input("Skype: ")
diachi = input("Địa chỉ: ")
noilam = input("Nơi làm việc: ")

# Ghi file
with open("setInfo.txt", "w", encoding="utf-8") as f:
    f.write(f"Tên: {ten}\n")
    f.write(f"Tuổi: {tuoi}\n")
    f.write(f"Email: {email}\n")
    f.write(f"Skype: {skype}\n")
    f.write(f"Địa chỉ: {diachi}\n")
    f.write(f"Nơi làm việc: {noilam}\n")

# Đọc lại
print("\n--- Nội dung file ---")
with open("setInfo.txt", "r", encoding="utf-8") as f:
    print(f.read())