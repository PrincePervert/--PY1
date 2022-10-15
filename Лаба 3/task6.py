list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

f_max_index = 0
for i in range(len(list_numbers)):
    max_number = list_numbers[f_max_index]
    number = list_numbers[i]
    if number > max_number:
        f_max_index = i

list_numbers[f_max_index], list_numbers[-1] = list_numbers[-1], list_numbers[f_max_index]

print(list_numbers)
