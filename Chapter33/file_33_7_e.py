a = [3, 6, 10, 2, 1, 12, 4]
b = sorted(a)

for element in a:
    print(element, end = " ") # 출력: 3, 6, 10, 2, 1, 12, 4
print()

for element in b:
    print(element, end = " ") # 출력: 1 2 3 4 6 10 12
print()

c = ["Hermes", "Apollo", "Dionysus"]
for element in sorted(c, reverse = True):
    print(element, end = " ") # 출력: Hermes Dionysus Apollo