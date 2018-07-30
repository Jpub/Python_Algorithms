w = int(input("몸무게값을 입력하여라: "))
maximum = w

for i in range(9):
    w = int(input("몸무게값을 입력하여라: "))
    if w > maximum:
        maximum = w

print(maximum)
