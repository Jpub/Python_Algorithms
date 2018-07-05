a = [3, 6, 10, 2, 1, 12, 4]
a.sort()
for element in a:
    print(element, end = " ") # 출력: 1 2 3 4 6 10 12

print()

# 내림차순 정렬
a.sort(reverse = True)
for element in a:
    print(element, end = " ") # 출력: 12 10 6 4 3 2 1

print()
b = [ [4, 6, 8], \
[3, 11, 9], \
[2, 9, 1]
]

# 마지막 열 정렬
b[2].sort()

for row in b:
    for element in row:
        print(element, end = " ") # 출력: 4 6 8
                                  #      3 11 9
                                  #      1 2 9
print() 

c = ["Hermes", "Apollo", "Dionysus"]
c.sort()
for element in c:
    print(element, end = " ") # 출력: Apollo Dionysus Hermes
