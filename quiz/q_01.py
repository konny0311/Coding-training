def convert_decimal2binary(num):
    mod_list = []
    x = num
    while x != 0:
        q, mod = divmod(x, 2)
        mod_list.append(mod)
        x = q
    mod_list.reverse()
    binary = ''
    for mod in mod_list:
        binary += str(mod)
    return binary

def convert_decimal2octa(num):
    mod_list = []
    x = num
    while x != 0:
        q, mod = divmod(x, 8)
        mod_list.append(mod)
        x = q
    mod_list.reverse()
    binary = ''
    for mod in mod_list:
        binary += str(mod)
    return binary

def is_palindrome(num_str):
    for i in range(len(num_str)):
        i_from_end = -(i+1)
        if num_str[i] != num_str[i_from_end]:
            return False
    return True

find = False
for i in range(10, 1000):
    decimal_num = i
    binary_num = convert_decimal2binary(decimal_num)
    octal_num = convert_decimal2octa(decimal_num)
    if is_palindrome(str(decimal_num)) and is_palindrome(binary_num) and is_palindrome(octal_num):
        print(decimal_num)
        find = True
        break

if not find:
    print('palindrome not find')