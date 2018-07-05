ELEMENTS = 5

def get_num_of_digits(x, index):
    count = 0
    
    aux_var = x[index]
     
    while aux_var != 0:
        count += 1
        aux_var = aux_var // 10
    return count

# 메인 코드
val = [None] * ELEMENTS

for i in range(ELEMENTS):
    val[i] = int(input())
    
for i in range(ELEMENTS):
    print(get_num_of_digits(val, i), "은/는", val[i], "의 자릿수입니다.")
