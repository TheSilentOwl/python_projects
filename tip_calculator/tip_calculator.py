print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

def index_of(string, char):
    counter = 0
    for element in string:
        if element == char:
            return counter
        counter += 1
    return -1

def split_str(string, separator):
    splitted_str = []
    separator_index = 0
    while separator_index != -1:
        separator_index = index_of(string,separator)
        if separator_index == -1:
            splitted_str.append(string[0::])
            string = ""
        else:
            splitted_str.append(string[0: separator_index])
            string = string[separator_index + 1::]
    return splitted_str

def format_num(num, decimal_num):
    numStr = str(num)
    splittedStr = split_str(numStr, ".")
    integer = splittedStr[0]
    decimal = splittedStr[1]
    if len(decimal) >= 2:
        decimal = decimal[0: 2]
    else:
        decimal = decimal + "0" * (int(decimal_num) - len(decimal))
    return integer + "." + decimal

# def format_num(num, decimal_num):
#     numStr = str(num)
#     splittedStr = numStr.split(".")
#     integer = splittedStr[0]
#     decimal = splittedStr[1]
#     if len(decimal) >= 2:
#         decimal = decimal[0: 2]
#     else:
#         decimal = decimal + "0" * (int(decimal_num) - len(decimal))
#     return integer + "." + decimal


payment = (bill / people) * (1 + tip / 100)
print(format_num(payment, 2))






