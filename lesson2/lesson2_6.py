print('inpunt A: ')
A = int(input())
print('inpunt B: ')
B = int(input())

sum1 = A ** 2 + B ** 2
sum2 = (A + B) ** 2

if sum1 > sum2:
    print('the sum of the squares is greater')
else:
    print('the squares of the sum is greater')
