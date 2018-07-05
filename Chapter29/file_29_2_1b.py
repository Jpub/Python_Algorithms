x = int(input("한 자릿수 정수(0 - 9)를 입력하여라: "))

for i in range(100, 1000):
    digit3, r = divmod(i, 100)
    digit2, digit1 = divmod(r, 10)

    if x in [digit1, digit2, digit3]:
        print(i)
