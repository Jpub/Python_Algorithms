def test_integer(number):
    return_value = False

    if number == int(number):
        return_value = True
    return return_value

# 메인 코드
total = 0
count = 0
x = float(input())
while test_integer(x) == True:
    if x > 0:
        total += x
        count += 1
    x = float(input())

if count > 0:
    print(total / count)
