def my_divmod(a, b, results):
    return_value = True

    if b == 0:
        return_value = False
    else:
        results[0] = a // b
        results[1] = a % b
    
    return return_value

# 메인 코드
res = [None] * 2

val1 = int(input())
val2 = int(input())
ret = my_divmod(val1, val2, res)
if ret == True:
    print(res[0], res[1])
else:      
    print("잘못된 입력값입니다!");
