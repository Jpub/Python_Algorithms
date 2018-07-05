count_a = 0
count_b = 0

for i in range(10):
    a = int(input("첫 번째 숫자를 입력하여라: "))
    b = int(input("두 번째 숫자를 입력하여라: "))

    if a > b:
        count_a += 1
    elif b > a:
        count_b += 1

print(count_a, count_b)
