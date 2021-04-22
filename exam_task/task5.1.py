N = 13

while N != 1:
    if N % 2 == 0:
        N = N // 2
    else:
        N = (N * 3 + 1) // 2
        print(N)


