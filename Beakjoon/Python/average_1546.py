import sys

input = sys.stdin.readline
num = int(input())
score = list(map(float, input().split()))
score.sort()
Max = score[num - 1]
for i in range(0, num, 1):
    score[i] = score[i] / Max * 100
avg = float(sum(score) / num)
print(avg)
