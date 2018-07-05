import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

inp = input()

if not re.match(IS_NUMERIC, inp):
    print("숫자가 아닙니다.")
else:
    x = int(inp)
    if x < 10000:
        print("5자릿수보다 작은 수입니다.")
    elif x > 99999:
        print("5자릿수보다 큰 수입니다.")
    else:
        digit1, r = divmod(x, 10000)
        digit2, r = divmod(r, 1000)
        digit3, r = divmod(r, 100)
        digit4, digit5 = divmod(r, 10)

        if digit1 == digit5 and digit2 == digit4:
            print("회문입니다.")
        else:
            print("회문이 아닙니다.")
