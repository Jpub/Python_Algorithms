def display_menu():
    print("1. 달러를 유로로 변환하기")
    print("2. 유로를 달러로 변환하기")
    print("3. 종료")
    print("----------------------------")
    print("선택하여라: ", end = "")

# 메인 코드
while True:
    display_menu()
    choice = int(input())

    if choice != 3:
        amount = float(input("금액을 입력하여라: "))
        if choice == 1:
            print(amount, "달러 =", amount * 0.72, "유로")
        else:
            print(amount, "유로 =", amount / 0.72, "달러")
    else:
        print("종료합니다.")
        break
