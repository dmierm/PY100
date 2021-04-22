def task_2(str_, src, dst):
    if src in str_:
        str_ = str_.replace(src, dst)
        print(str_)
    else:
        print('string was not change')



if __name__ == '__main__':
    s0 = 'abcdef'
    s1 = 'ab'
    s2 = '12'
    task_2(s0, s1, s2)