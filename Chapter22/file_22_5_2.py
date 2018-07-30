m = int(input("월을 입력하여라(1 - 12): "))
y = int(input("연도를 입력하여라: "))

if m == 2:
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print("입력한 월은 29일까지 있습니다.")
    else:
        print("입력한 월은 28일까지 있습니다.")
elif m == 4 or m == 6 or m == 9 or m == 11:
    print("입력한 월은 30일까지 있습니다.")
else:
    print("입력한 월은 29일까지 있습니다.")
