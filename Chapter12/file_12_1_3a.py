x = float(input("x 값을 입력하여라: "))
w = float(input("w 값을 입력하여라: "))
z = float(input("z 값을 입력하여라: "))

temp1 = 3 * x ** 2 + 5 * x + 2
temp2 = 7 * w - 1 / z
temp3 = (3 + x) / 7
nominator = 5 * temp1 / temp2 - z
denominator = 4 * temp3

y = nominator / denominator

print("결과:", y)
