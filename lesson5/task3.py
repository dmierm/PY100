def pow_n(a,n):
    result = 1
    i = 0
    while i != n:
        result *= a
        i += 1
    print(result)


if __name__ == '__main__':
    pow_n(2, 5)

