import sys

input = sys.stdin.readline
num = int(input())
# a = list(map(int, input().strip().split()))
# cnt = 0
# b = []
# c = []
# for i in range(num):
#     for j in range(num):
#         if a[i] > a[j]:
#             if a[j] not in c:
#                 c.append(a[j])
#                 cnt += 1
#             else:
#                 continue
#     c = []
#     b.append(cnt)
#     cnt = 0
# for i in b:
#     print(i, end=" ")
list_a = list(map(int, input().rstrip().split()))
b = set(list_a)
b = sorted(b)
c = {b[i]: i for i in range(len(b))}


for i in list_a:
    print(c[i], end=" ")
