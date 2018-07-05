x = int(input("한 자릿수 정수(0 - 9)를 입력하여라: "))

for digit3 in range(1, 10):
    for digit2 in range(10):
        for digit3 in range(10):
            if x in [digit1, digit2, digit3]:
                print(digit3 * 100 + digit2 * 10 + digit1)
