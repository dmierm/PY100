list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print('input k: ')
k = int(input())
list1_ = []
list2_ = []

#print(len(list_))
for i in range(len(list_)):
    i = i + k
    for i in range(k):
        list1_.append(k)
    list2_.append(list1_)


#   print(k)
#    list1_.append(i)
print(list2_)
