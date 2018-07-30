for i in range(100, 1000):
    digit3, r = divmod(i, 100)
    digit2, digit1 = divmod(r, 10)
    if digit3 < digit2 and digit2 < digit1:
        print(i)
