import sys

input = sys.stdin.readline

num = int(input())
dic = {}
for _ in range(num):
    a = input().replace("\n", "").strip()
    dic[a] = len(a)


d1 = sorted(dic.items(), key=lambda x: (x[1], x[0]))
for i in d1:
    print(i[0])
