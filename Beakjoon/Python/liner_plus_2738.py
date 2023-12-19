import sys

n, m = map(int, sys.stdin.readline().split())

a = []
for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    a.append(data)

# new = [[0] * m] * n #call by value call by reference 두개 기억
new = [[0 for _ in range(m)] for _ in range(n)]

b = []
for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    b.append(data)

for i in range(n):
    for j in range(m):
        new[i][j] = int(a[i][j]) + int(b[i][j])
print(new)
