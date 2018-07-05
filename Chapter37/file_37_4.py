def maximum(val1, val2):
    m = val1
    if val2 > m:
        m = val2
    return m

# 메인 코드가 여기서 시작된다.
a = float(input())
b = float(input())
maxim = maximum(a, b)
print(maxim)
