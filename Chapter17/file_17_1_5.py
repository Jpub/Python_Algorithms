pay_rate = float(input())
hours_worked = int(input())

if hours_worked <= 40:
    gross_pay = pay_rate * hours_worked
else:
    gross_pay = pay_rate * 40 + 1.5 * pay_rate * (hours_worked - 40)

print("급여:", gross_pay)
