def f1():
    test = 22
    print(test)
    return True

def f2(test):
    print(test)

# 메인 코드
test = 5
print(test)
ret = f1()
f2(10)
print(test)
