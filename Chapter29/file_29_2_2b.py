for digit3 in range(1, 10):
    for digit2 in range(10):
        for digit1 in range(10):
            if digit3 < digit2 and digit2 < digit1:
                print(digit3 * 100 + digit2 * 10 + digit1)
