print("소포의 무게와 목적지를 입력하여라: ")
weight = float(input())
dest = input()

if dest.upper() == "I":
    if weight <= 1:
        cost = weight * 1000
    elif weight <= 2:
        cost = weight * 1300
    elif weight <= 4:
        cost = weight * 1500
    else:
        cost = weight * 2000
else:
    if weight <= (1):
        cost = 10000
    elif weight <= 2:
        cost = 20000
    elif weight <= 4:
        cost = 50000
    else:
        cost = 60000

print("배송비:", cost)
