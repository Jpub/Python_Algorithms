import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

while True:
    inp = input("0과 100 사이의 실수값을 입력하여라: ")
    if re.match(IS_NUMERIC, inp) and 0 <= float(inp) <= 100: break

x = float(inp)

best_n = 1
best_m = 1
for n in range(101):
    for m in range(1, 101):
        if abs(n / m - x) < abs(best_n / best_m - x):
            best_n = n
            best_m = m

print("분수:", best_n, "/", best_m)
