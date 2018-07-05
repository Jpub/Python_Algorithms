def display_menu():
    print("1. USD를 EUR로 변환")
    print("2. USD를 GBP로 변환")
    print("3. USD를 JPY로 변환")
    print("4. USD를 CAD로 변환")
    print("5. 종료")
    print("----------------------------------------------")
    print("메뉴를 선택하여라: ", end = "")

def USD_to_EU(value):
    return value * 0.72

def USD_to_GBP(value):
    return value * 0.6

def USD_to_JPY(value):
    return value * 102.15

def USD_to_CAD(value):
    return value * 1.1

# 메인 코드
while True:
    display_menu()
    choice = int(input())

    if choice == 5:
        print("종료!")
        break
    else:
        amount = float(input("금액을 입력하여라(USD): "))
        if choice == 1:
            print(amount, "USD =", USD_to_EU(amount), "EUR")
        elif choice == 2:
            print(amount, "USD =", USD_to_GBP(amount), "GBP")
        elif choice == 3:
            print(amount, "USD =", USD_to_JPY(amount), "JPY")
        elif choice == 4:
            print(amount, "USD =", USD_to_CAD(amount), "CAD")
