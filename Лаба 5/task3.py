from random import randint


def get_unique_list_numbers() -> list[int]:
    number_list = []
    while len(number_list) < 15:
        num = randint(-10, 10)
        if num not in number_list:
            number_list.append(num)
    return number_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
