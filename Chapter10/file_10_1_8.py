VAT = 0.19

price_before_discount = float(input("상품 가격을 입력하여라: "))
discount = int(input("할인율을 입력하여라(0 - 100): "))

discount_amount = price_before_discount * discount / 100
price_after_discount = price_before_discount - discount_amount

sales_tax = price_after_discount * VAT
price_after_tax = price_after_discount + sales_tax

print("최종 상품 가격:", price_after_tax)