from pprint import pprint

nums = 16

list_of_num_dictionaries = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(nums)]

pprint(list_of_num_dictionaries)
