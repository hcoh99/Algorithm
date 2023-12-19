import sys

input = sys.stdin.readline
res = 0
paper = [[0 for _ in range(100)] for _ in range(100)]
num = int(input())
for _ in range(num):
    x, y = list(map(int, input().split()))
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            paper[i][j] = 1
for k in range(100):
    res += paper[k].count(1)  # 리스트 내에서 1을찾는것 그러므로 슬라이싱 해서 넣어줌.
print(res)
