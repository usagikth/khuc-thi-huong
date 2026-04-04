# Ghi file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Xin chào Python!\nHọc lập trình rất thú vị.")

# Đọc lại file
with open("output.txt", "r", encoding="utf-8") as f:
    print(f.read())