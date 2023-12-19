import sys

algebra = []
for _ in range(9):
    a = list(map(int, sys.stdin.readline().split()))
    algebra.append(a)
maxi = algebra[0][0]
a = b = 0
for i in range(9):
    for j in range(9):
        if algebra[i][j] > maxi:
            maxi = algebra[i][j]
            a, b = i, j
print(maxi)
print(a + 1, b + 1)
