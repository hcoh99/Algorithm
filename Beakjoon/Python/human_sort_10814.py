import sys

input = sys.stdin.readline
num = int(input())
b = []
for i in range(num):
    a = list(map(str, input().rstrip().split()))
    a.append(i)
    a[0] = int(a[0])
    b.append(a)

b.sort(key=lambda x: (x[0], x[2]))
print(b)
for a, n, k in b:
    print(a, n)
