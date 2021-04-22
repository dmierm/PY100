#Ввести с клавиатуры три числа, положительные возвести в квадрат, а отрицательные оставить без изменений.

n = []
print('input three numbers:')
for i in range(3):
    a = int(input())
    n.append(a ** 2 if a > 0 else a)

print(n)

#n.append(a**2 if a > 0 else o)