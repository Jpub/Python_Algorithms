import re
import random
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"
ACCURACY = 0.0000000000001

inp = input("음수가 아닌 숫자를 입력하여라: ")
while not re.match(IS_NUMERIC, inp) or float(inp) < 0:
    inp = input("올바르지 않은 값입니다. 음수가 아닌 숫자를 입력하여라: ")
    
y = float(inp)
    
guess = random.randrange(1, y + 1)           # 첫 번째 추측값을 1과 입력값
                                             # 사이에서 무작위로 생성

while abs(guess * guess - y) > ACCURACY:     # 충분히 가까운가?
    guess = (guess + y / guess) / 2          # 그렇지 않으면 새로운 추측값을 생성!
print(guess)
