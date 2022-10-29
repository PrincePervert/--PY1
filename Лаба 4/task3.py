def delete(list_, index=None):
    if len(list_) == 0:
        return 'Список пуст, удалять нечего :('
    elif len(list_) == 1:
        if index == 0:
            return 'Вы удалили последнее значение из списка'
        return 'Индекс выходит за пределы списка'
    elif index is not None:
        if index <= len(list_) - 1:
            pre_list = list_[:index]
            post_list = list_[index+1:]
            pre_list.extend(post_list)
            return pre_list
        return 'Индекс выходит за пределы списка'
    list_.pop()
    return list_


print(delete([0, 0, 1, 2], index=0))       # [0, 1, 2]
print(delete([0, 1, 1, 2, 3], index=1))    # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4]))          # [0, 1, 2, 3, 4]

# print(delete([0, 1, 1, 2, 3], index=5))  # Индекс выходит за пределы списка
# print(delete([0], index=0))              # Вы удалили последнее значение из списка
# print(delete([0], index=1))              # Индекс выходит за пределы списка
# print(delete([]))                        # Список пуст, удалять нечего :(
# print(delete([], index=1))               # Список пуст, удалять нечего :(
