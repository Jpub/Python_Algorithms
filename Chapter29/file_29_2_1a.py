x = int(input("한 자릿수 정수(0 - 9)를 입력하여라: "))

for i in range(100, 1000):
    digit3 = i // 100
    r = i % 100

    digit2 = r // 10
    digit1 = r % 10

    if digit3 == x or digit2 == x or digit1 == x:
        print(i)
