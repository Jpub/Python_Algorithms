while True:
    print("두 개의 숫자를 입력하여라: ")
    a = int(input())
    b = int(input())

    result = a ** b
    print("결과: ", result)

    answer = input("반복하시겠습니까? ")
    if answer.upper() != "YES": break
