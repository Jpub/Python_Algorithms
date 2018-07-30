import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

inp = input("연도를 입력하여라: ")

if not re.match(IS_NUMERIC, inp):
    print("입력한 값은 숫자가 아닙니다.")
else:
    y = int(inp)
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print("윤년입니다.")
    else:
        print("윤년이 아닙니다.")
