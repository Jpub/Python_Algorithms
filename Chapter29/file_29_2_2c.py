for digit3 in range(1, 8):
    for digit2 in range(digit3 + 1, 9):
        for digit1 in range(digit2 + 1, 10):
            print(digit3 * 100 + digit2 * 10 + digit1)
