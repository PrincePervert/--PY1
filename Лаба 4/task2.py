def get_count_char(str_):
    lowercase = str_.lower()
    dict_ = dict()
    for i in lowercase:
        if i.isalpha():
            dict_[i] = dict_.get(i, 0) + 1
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print('Частота встречающихся символов в вышеуказанной строке:')
print(get_count_char(main_str))

# Замена количества элементов на %-ое отношение к сумме количества всех элементов (3 знака после ,)


def get_percent_char(old_dict):
    new_dict = dict()
    sum_ = sum(old_dict.values())
    for k, v in old_dict.items():
        percentage = round(v * 100 / sum_, 3)
        new_dict[k] = new_dict.get(k, percentage)
    return new_dict


print('\nПроцентное отношение количества каждого символа вышеуказанной строки к общему числу символов данной строки:')
print(get_percent_char(get_count_char(main_str)))
