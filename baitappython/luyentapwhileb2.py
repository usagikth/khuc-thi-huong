n = int(input("Nhập n: "))

i = 1
giaithua = 1

while i <= n:
    giaithua *= i
    i += 1

print("n! =", giaithua)