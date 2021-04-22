def is_pow_n(a, n = 2):
    while True:
        over = a % n
        if over != 0:
            break
        new_a = a // n
        if a == 1:
            is_pow = True
            break

    return is_pow


if __name__ == '__main__':
    print(is_pow_n(pow_n(2, 5)))


