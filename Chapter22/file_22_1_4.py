COEFFICIENT = 3.785

print("1: 갤런을 리터로 바꾸기")
print("2: 리터를 갤런으로 바꾸기")
choice = int(input("메뉴를 선택하여라: "))

quantity = float(input("양을 입력하여라: "))

if choice == 1:
    result = quantity * COEFFICIENT
    print(quantity, "갤런 =", result, "리터")
else:
    result = quantity / COEFFICIENT
    print(quantity, "리터 =", result, "갤런")
