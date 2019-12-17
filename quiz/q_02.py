M = ['*', '/', '+', '-']

def reverse_number(num):
    str_num = str(num)
    return ''.join(list(reversed(str_num)))

def count_single(num, num_reverse):
    num_str = str(num)
    flag = False
    final_res = []
    for i in range(1, 3):
        first = int(num_str[:i])
        second = int(num_str[i:])
        for each in M:
            if each == '/' and second == 0:
                continue
            final_res.append(str(eval('{} {} {}'.format(first, each, second))))
        for each in final_res:
            if each == num_reverse:
                flag = True

    return flag

def count_double(num, num_reverse):
    num_str = str(num)
    flag = False
    for pair in [(1, 3), (2, 3), (1, 2)]:
        first = int(num_str[:pair[0]])
        second = int(num_str[pair[0]:pair[1]])
        third = int(num_str[pair[1]:])
        final_res = []
        for m_1 in M:
            for m_2 in M:
                if m_1 == '/' and second == 0:
                    continue
                if m_2 == '/' and third == 0:
                    continue
                final_res.append(str(eval('{} {} {} {} {}'.format(first, m_1, second, m_2, third))))
        for each in final_res:
            if each == num_reverse:
                flag = True
    return flag

def count_triple(num, num_reverse):
    num_str = str(num)
    final_res = []
    flag = False
    for m_1 in M:
        for m_2 in M:
            for m_3 in M:
                if m_1 == '/' and int(num_str[1]) == 0:
                    continue
                if m_2 == '/' and int(num_str[2]) == 0:
                    continue
                if m_3 == '/' and int(num_str[3]) == 0:
                    continue
                final_res.append(str(eval('{} {} {} {} {} {} {}'.format(int(num_str[0]), m_1, int(num_str[1]), m_2, int(num_str[2]), m_3, int(num_str[3])))))
    for each in final_res:
        if each == num_reverse:
            flag = True
    return flag

for i in range(1000, 10000):
    i_reverse = reverse_number(i)
    if count_single(i, i_reverse):
        print(i)
    if count_double(i, i_reverse):
        print(i)
    if count_triple(i, i_reverse):
        print(i)
