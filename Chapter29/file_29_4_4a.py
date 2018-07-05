x = int(input())

number_of_divisors = 0
for i in range(1, x + 1):
    if x % i == 0:
        number_of_divisors += 1
        
print(number_of_divisors)
