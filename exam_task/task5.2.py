# Начав тренировки, спортсмен в первый день пробежал n км. Каждый день он увеличивал дневную норму на
# y% нормы предыдущего дня. Какой суммарный путь пробежит спортсмен за x дней?

def training(n, y, x):
    days = 0
    while days <= x:
        days += 1
        n = n + (y / 100) * n
    print(n)

    print('answer:', days, )


n = 5
y = 10
x = 5

training(n, y, x)
