import random

last_name = input("당신의 영문 성 이름을 입력하여라: ")

# 100과 999 사이의 랜덤 정수를 얻는다.
random_int = random.randrange(100, 1000)

print(last_name[:4].lower() + str(random_int))
