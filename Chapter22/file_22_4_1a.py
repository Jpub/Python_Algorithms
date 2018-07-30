amount = float(input("주문액을 입력하여라: "))

if amount < 30000:
    discount = 0
elif amount >= 30000 and amount < 70000:
    discount = 5
elif amount >= 70000 and amount < 150000:
    discount = 10
elif amount >= 150000:
    discount = 20

payment = amount - amount * discount / 100

print("할인율: ", discount, "%", sep = "")
print("지불액: ", payment, "원", sep = "")
