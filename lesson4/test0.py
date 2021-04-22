def task_1(str_1, str_2, k):
    result = str_1[:k] == str_2[:k]

    answer = 'Yes' if result else 'No'
    print(answer)

if __name__ == '__main__':
    s1 = 'abcd'
    s2 = 'abc'
    task_1(s1, s2, 4)
