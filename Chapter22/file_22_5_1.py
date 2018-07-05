import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

inp = input("연도를 입력하여라: ")

if not re.match(IS_NUMERIC, inp):
    print("올바르지 않은 값입니다.")
else:
    y = int(inp)
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print("윤년입니다.")
    else:
        print("윤녕이 아닙니다.")
