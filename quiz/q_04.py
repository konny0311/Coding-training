def cut_bar(n, m , current):
    if current > n:
        return 0
    elif current < m:
        current += current
        return 1 + cut_bar(n, m, current)
    else:
        current += m
        return 1 + cut_bar(n, m, current)

print(cut_bar(100, 5, 1))

    






# M = 3
# N = 20
# m = [0 , 0, 0]
# n = [N]
# total_cnt = 0
# while True:
#     tmp_n = n.copy()
#     if len(tmp_n) == 1 and tmp_n[0] % 2 == 0:
#         n = [N/2, N/2]
#     if len(tmp_n) == 1 and tmp_n[0] % 2 != 0:
#         n = [N//2, (N//2) + 1]
#     else:
#         cnt = 0
#         if max(tmp_n) == 1:
#             break
#         if max(tmp_n) < 4:
#             for i, each in enumerate(tmp_n):
#                 if each != 1 and cnt < M:
#                     if each % 2 == 0:
#                         n[i] = each/2
#                         n.append(each/2)
#                     else:
#                         n[i] = each//2
#                         n.append((each//2)+1)
#                     cnt += 1
#         else:
#             for i, each in enumerate(tmp_n):
#                 if each > 3 and cnt < M:
#                     if each % 2 == 0:
#                         n[i] = each/2
#                         n.append(each/2)
#                     else:
#                         n[i] = each//2
#                         n.append((each//2)+1)
#                     cnt += 1
#         total_cnt += cnt
#     print(tmp_n)
#     print(total_cnt)
# print('\n---result---')
# print(n)


    