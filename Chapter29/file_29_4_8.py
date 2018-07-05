ACCURACY = 0.00001

pi = 0

sign = 1         # 첫 번째 분수의 부호
denom = 1        # 첫 번째 분수의 분모
while True:
    pi_previous = pi
    pi += sign * 4 / denom
    sign = -sign
    denom += 2
    if abs(pi - pi_previous) <= ACCURACY: break   # 충분히 가까운가?

print("Pi ~=", pi)
