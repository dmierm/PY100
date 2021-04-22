#Найти количество и произведение отрицательных элементов, а также сумму нечетных элементов.

N = 5
list_ = [int(input()) for i in range(N)]
# i - что положить, for i in range(N)- где взять; при каком условии if i % 2 != 0 and i % 5 == 0
print(list_)
x = 0
count = 0
mult = 1
sum_ = 0
for x in list_:
    if x < 0:
        count += 1
        mult = mult * x
    elif x % 2 != 0:
        sum_ = sum_ + x

print('количество отрицательных элементов:', count, 'их произведение:', mult)
print('сумма нечетных элементов:', sum_)






