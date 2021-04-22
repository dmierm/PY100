#Задано натуральные числа от 10 до N. Вывести нечетные кратные пяти числа.

# list_ = []
N = 100
i = 10
list_ = []
for i in range(N):
    if i % 2 != 0 and i % 5 == 0:
        list_.append(i)

list_ = [i for i in range(N) if i % 2 != 0 and i % 5 == 0]
# i - что положить, for i in range(N)- где взять; при каком условии if i % 2 != 0 and i % 5 == 0
print(list_)
