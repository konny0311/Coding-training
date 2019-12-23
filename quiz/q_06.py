def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def is_collatz(ori_num, tmp_num, is_first):
    while True:
        if not is_first and (tmp_num == ori_num):
            return True
        if tmp_num == 1:
            return False
        if (is_even(tmp_num) and is_first) or not is_even(tmp_num):
            processed_num = (3 * tmp_num) + 1
            return is_collatz(ori_num, processed_num, False)
        if is_even(tmp_num):
            processed_num = tmp_num / 2
            return is_collatz(ori_num, processed_num, False)

cnt = 0
for i in range(2, 10001, 2):
    if is_collatz(i, i, True):
        cnt += 1
print(cnt)

