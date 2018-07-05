amount = float(input("주문액을 입력하여라: "))

if amount < 30000:
    discount = 0
elif amount < 70000:
    discount = 5
elif amount < 150000:
    discount = 10
else:
    discount = 20

payment = amount - amount * discount / 100

print("할인률: ", discount, "%", sep = "")
print("지불액: ", payment, "원", sep = "")
