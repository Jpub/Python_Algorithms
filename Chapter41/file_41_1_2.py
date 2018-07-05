def test_integer(number):
    return_value = False
    
    if number == int(number):
        return_value = True
    return return_value

def test_odd(number):
    return_value = False

    if number % 2 != 0:
        return_value = True
    return return_value

def test_positive(number):
    return_value = False

    if number > 0:
        return_value = True
    return return_value

# 메인 코드
total = 0
x = float(input())
while test_positive(x) == True:
    if test_integer(x) == True and test_odd(x) == True:
        total += x
    x = float(input())

print(total)
