def task_1():
    s = float(input("Input deposit sum: "))

    p = None
    if s < 5000:
        p = 20
    elif 5000 <= s < 10000:
        p = 22
    else:
        p = None
    print(p)

if __name__ = '__main__':
    task_1()
