from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())
a = []
check = {}
for _ in range(n):
    b = int(input())
    a.append(b)
    # check[b] = 0
print(round(sum(a) / n))
print(sorted(a)[n // 2])
# for i in a:
#    check[i] += 1
# number = set(a)
# cnt_lis = []
# cnt_num = 0
# for i in number:
#     if cnt_num == a.count(i):
#         cnt_lis.append(i)
#     elif cnt_num < a.count(i):
#         cnt_lis = []
#         cnt_lis.append(i)
#         cnt_num = a.count(i)
# if len(cnt_lis) > 1:
#     cnt_lis.sort()
#     print(cnt_lis[1])
# else:
#     print(cnt_lis[0])
cnt = Counter(a).most_common()
if len(a) > 1:

    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

# print(sorted(check.values())[len(check) - 1])
print(max(a) - min(a))
