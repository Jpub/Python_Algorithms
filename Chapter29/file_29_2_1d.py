x = input("한 자릿수 정수(0 - 9)를 입력하여라: ")

for i in range(100, 1000):
    digit3, digit2, digit1 = str(i)
    if x in [digit3, digit2, digit1]:
        print(i)
