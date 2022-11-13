import string
from random import sample

length = 8


def get_random_password() -> str:
    available_symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
    random_pass_list = sample(available_symbols, length)
    random_password = ''.join(str(symbol) for symbol in random_pass_list)
    return random_password


print(get_random_password())
