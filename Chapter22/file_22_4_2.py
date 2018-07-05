import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

inp = input("주문액을 입력하여라: ")

if not re.match(IS_NUMERIC, inp):
    print("입력한 값은 숫자가 아닙니다.")
else:
    amount = float(inp)
    if amount < 0:
        print("입력한 값이 음수입니다.")
    else:
        if amount < 30000:
            discount = 0
        elif amount < 70000:
            discount = 5
        elif amount < 150000:
            discount = 10
        else:
            discount = 20
        payment = amount - amount * discount / 100

        print("할인액: ", discount, "%", sep = "")
        print("지불액: ", payment, "원", sep = "")
