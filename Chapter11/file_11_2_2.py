import math

a = float(input("가속도값을 입력하여라: "))
S = float(input("주행 거리를 입력하여라: "))

t = math.sqrt(2 * S / a)

print("주행 시간(초):", t)
