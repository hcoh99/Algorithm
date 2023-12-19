def d(n):
    res = 0
    for i in range(len(str(n))):
        res += int(str(n)[i])
    res = res + n
    return res


full_list = [i for i in range(1, 10000)]

rs = []
for k in range(1, 10001):
    if d(k) < 10000 and d(k) in full_list:
        full_list.remove(d(k))

for j in full_list:

    print(j)
