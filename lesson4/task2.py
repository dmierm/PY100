def task_3():
    print()




if __name__ == '__main__':
    main_str = """
Данное предложение будет разбиваться на отдельные слова. 
В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
    list_words = main_str.split(' ')
    replace_punctuation = '.,!'
    for i, word in enumerate(list_words):
        for punc in replace_punctuation:
            word = word.replace(punc, '')
            list_words[i] = word

    print(list_words)
    print(type(list_words))
