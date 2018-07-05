x = int(input("1보다 큰 정수를 입력하여라: "))

number_of_divisors = 2
i = 2
while i <= x // 2 and number_of_divisors == 2:
    if x % i == 0:
        number_of_divisors += 1
    i += 1

if number_of_divisors == 2:
    print("숫자", x, "은/는 소수입니다.")
