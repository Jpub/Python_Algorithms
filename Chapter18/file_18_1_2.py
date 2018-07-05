x = int(input("정수를 입력하여라(0 - 999): "))

if x <= 9:
    count = 1
elif x <= 99:
    count = 2
else:
    count = 3

print("자릿수:", count)
