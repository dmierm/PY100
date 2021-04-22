def task_6():
    print()

if __name__ == '__main__':
    main_str = """
Данное предложение будет разбиваться на отдельные слова. 
В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

    dict_char = {}
    for char in main_str:
        
        if char not in dict_char:
            dict_char[char] = 1
        else:
            dict_char[char] += 1

    for symbol, count in dict_char.items():
        print(symbol, count)