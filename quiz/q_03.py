def turn(num):
    if num == 0:
        return 1
    else:
        return 0

l = [0] * 100
for n in range(1, 100):
    target = n
    while target <= 99:
        l[target] = turn(l[target])
        target += (n + 1)
print([i+1 for i, x in enumerate(l) if x == 0])
