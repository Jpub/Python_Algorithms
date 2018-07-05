import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

def get_consumption():
    inp = input("전력 소비량을 입력하여라(kWh): ")
    while not re.match(IS_NUMERIC, inp) or int(inp) < 0:
        print("오류: 올바르지 않은 입력값입니다.")
        inp = input("양수를 입력하여라: ")
    return int(inp)


def find_amount(kwh):
    if kwh <= 400:
        amount = kwh * 0.08
    elif kwh <= 2000:
        amount = 400 * 0.08 + (kwh - 400) * 0.22
    elif kwh <= 4000:
        amount = 400 * 0.08 + 1100 * 0.22 + (kwh - 1500) * 0.35
    else:
        amount = 400 * 0.08 + 1100 * 0.22 + 1500 * 0.35 + (kwh - 3000) * 0.5

    amount += 0.26 * amount
    return amount

# 메인 코드

while True:
    kwh = get_consumption()
    print("총 전기요금:", find_amount(kwh))
    answer = input("반복할까요? ")
    if answer.upper() != "YES": break
