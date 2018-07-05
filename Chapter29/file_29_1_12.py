x = int(input("숫자를 입력하여라: "))
count = 0

while x != 0:
    count += 1
    x = x // 10

print(count)
