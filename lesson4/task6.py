N = 123456789

#print(list(str(N)))
list_digit = [int(d) for d in str(N)]
print(list_digit)

s = 0
for d in list_digit:
    s += d
sum(list_digit)

list_digit = sum([d for d in list_digit if d % 2 == 0])

list_even = []
for i, d in enumerate(list_digit):
    if i % 2 == 0:
        list_even.append(d)

list_even = list_digit[1::2]
