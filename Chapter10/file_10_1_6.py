VAT = 0.19
price_before_tax = float(input("상품의 세전 가격을 입력하여라: "))

sales_tax = price_before_tax * VAT
price_after_tax = price_before_tax + sales_tax

print("세후 가격:", price_after_tax)