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
        inp_reversed = inp[::-1]
        if inp == inp_reversed:
            print("회문입니다.")
        else:
            print("회문이 아닙니다.")
