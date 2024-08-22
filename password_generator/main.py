import random as rd
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# easy password
# ================
def easy_password(n_letts, n_syms, n_nums):
    password = ""
    for j in range(0, n_letts):
        password += letters[rd.randint(0, n_letts - 1)]
    for j in range(0, n_syms):
        password += symbols[rd.randint(0, n_syms - 1)]
    for j in range(0, n_nums):
        password += numbers[rd.randint(0, n_nums - 1)]

    return password



# hard password: hard way
# =======================
def index_of(iterable, char):
    counter = 0
    for element in iterable:
        if element == char:
            return counter
        counter += 1
    return -1

def random_indexes(iterable_chars):
    """used to shuffle the indexes of some iterable"""
    random_indexes_list = []
    while len(random_indexes_list) < len(iterable_chars):
        random_char_num = rd.randint(0, len(iterable_chars) - 1)
        if index_of(random_indexes_list, random_char_num) == -1:
            random_indexes_list.append(random_char_num)
    return random_indexes_list

def hard_password(password):
    new_indexes = random_indexes(password)
    new_password = ""
    for random_i in new_indexes:
        new_password += password[random_i]
    return new_password

# the_easy_password = easy_password(nr_letters, nr_symbols, nr_numbers)
# print("Your Password is: " + hard_password(easy_password))

# hard password: easy way
# ========================

easy_password_list = list(easy_password(nr_letters, nr_symbols, nr_numbers))
rd.shuffle(easy_password_list)
shuffled_password = easy_password_list
print("Your Password is: " + "".join(easy_password_list))

# print(hard_password(easy_password))





#
# characters = [letters, symbols, numbers]
# char_numbers = [nr_letters, nr_symbols, nr_numbers]
#
# total_char_count = nr_letters + nr_symbols + nr_numbers
# max_char_number = max(nr_letters, nr_symbols, nr_numbers)



