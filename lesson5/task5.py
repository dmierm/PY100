def task_5():
    S = 1000
    A = 100
    B = 120
    sum_ = S
    k = 0
    while True:
        sum_ += A
        sum_ -= B
        if sum_ < 0:
            break
        else:
            k += 1
            B = B + B * 0.03
    print(k)
    return k

