count = int(input("송신 메시지의 수를 입력하여라: "))

if count <= 50:
    extra = 0
elif count <= 150:
    extra = (count - 50) * 50
else:
    extra = 100 * 60 + (count - 150) * 90

total_without_tax = 80000 + extra
tax = total_without_tax * 10 / 100
total = total_without_tax + tax
print("지불해야 할 총 금액:", total)
