count = 0

x = float(input("숫자를 입력하여라: "))
while int(x) == x:
    if x > 0:
        count += 1
    x = float(input("숫자를 입력하여라: "))

print(count)
