import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

inp = input("전력 소비량을 입력하여라(kWh): ")

if not re.match(IS_NUMERIC, inp):
    print("입력한 값은 숫자가 아닙니다.")
else:
    kwh = int(inp)
    if kwh < 0:
        print("입력한 값은 음수입니다.")
    else:
        if kwh <= 500:
            t = kwh * 100
        elif kwh <= 2000:
            t = 250 * kwh - 75000
        elif kwh <= 4000:
            t = 400 * kwh - 375000
        else:
            t = 600 * kwh - 1175000

        t = 1.10 * t	# 이 명령문은 t = t + (t * 10 / 100)과 동일함

        print("세금을 포함한 총 지불액:", t)
