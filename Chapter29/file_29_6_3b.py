CITIZENS = 1000

total_yes = 0
female_no = 0
for i in range(CITIZENS):
    while True:
        sex = input("성별을 입력하여라: ").lower()
        if sex in ["m", "f"]: break

    while True:
        answer = input("아침식사를 하십니까? ").lower()
        if answer in ["y", "n", "s"]: break

    if answer == "y":
        total_yes += 1
    elif sex == "f":
        female_no += 1
        
print(total_yes, female_no * 100 / CITIZENS)
