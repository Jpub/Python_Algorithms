ELEMENTS = 5

def get_num_of_digits(x, index):
    count = 0
    while x[index] != 0:
        count += 1
        x[index] = x[index] // 10
    return count

# 메인 코드
val = [None] * ELEMENTS

for i in range(ELEMENTS):
    val[i] = int(input())
    
for i in range(ELEMENTS):
    print(get_num_of_digits(val, i), "은/는", val[i], "의 자릿수입니다.")
