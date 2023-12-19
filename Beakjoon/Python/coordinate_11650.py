import sys

input = sys.stdin.readline
num = int(input())
chk = []
for _ in range(num):
    chk.append(list(map(int, input().split())))
# for i in range(1, num):
#     for j in range(0, i):
#         if chk[i][0] < chk[j][0]:
#             chk[i], chk[j] = chk[j], chk[i]
#         if chk[i][0] == chk[j][0]:
#             if chk[i][1] < chk[j][1]:
#                 chk[i], chk[j] = chk[j], chk[i]
chk.sort(key=lambda x: (x[0], x[1]))

for i in chk:
    print(*i)
