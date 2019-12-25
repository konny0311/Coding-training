import datetime

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

def convert_binary2decimal(bin_num):
    decimal_num = 0
    str_bin_num = str(bin_num)
    length = len(str_bin_num)
    for i, each in enumerate(str_bin_num):
        if each == '1':
            decimal_num += 2 ** (length - (i + 1))
    return decimal_num

def reverse_binary(bin_num):
    str_bin_num = str(bin_num)
    num_list = [each for each in str_bin_num]
    num_list.reverse()
    res = ''
    for each in num_list:
        res += each
    return int(res)

cnt = 0
date = datetime.datetime(1964,10,10)
while True:
    date_num = int(date.strftime('%Y%m%d'))
    if date_num == 20200724:
        break
    processed_date = convert_decimal2binary(date_num)
    processed_date = reverse_binary(processed_date)
    processed_date = convert_binary2decimal(processed_date)
    if date_num == processed_date:
        print(date_num)
        cnt += 1
    date += datetime.timedelta(days=1)
print('total ', cnt)

