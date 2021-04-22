def my_join(list_str, sep):
    join_result =
    for str_ in list_str:
        join_result += str_
        join_result += sep
    last_word = list_str[-1]
    join_result += last_word

    return join_result




str_with_space = "    123.    test   print test11    "  # исходная строка
split_str = str_with_space.split(" ")

print(split_str)

split_str = [word for word in split_str if word != '']  #это тоже самое что и цикл ниже
#list_ = []
#for word in split_str:
#    list_.append(word)
print(split_str)

#my_join(split_str, "|") == "|".join(split_str)
#print(join_str)