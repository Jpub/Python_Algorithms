import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

inp = input()

if not re.match(IS_NUMERIC, inp):
    print("숫자가 아닙니다.")
else:
    inp_reversed = inp[::-1]
    if inp == inp_reversed:
        print("회문입니다.")
    else:
        print("회문이 아닙니다.")
