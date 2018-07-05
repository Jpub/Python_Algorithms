x = int(input())

number_of_divisors = 2
for i in range(2, x // 2 + 1):
    if x % i == 0:
        number_of_divisors += 1

print(number_of_divisors)
