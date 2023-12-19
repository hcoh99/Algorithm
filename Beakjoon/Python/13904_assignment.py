import sys

input = sys.stdin.readline
num = int(input())
hw = [list(map(int, input().split())) for _ in range(num)]
hw.sort()
res_hw = []
result = 0
for i in range(num, 0, -1):
    while hw and hw[-1][0] >= i:
        res_hw.append(hw.pop()[1])
    if res_hw:
        res_hw.sort()
        result += res_hw.pop()
    print(hw)
print(result)
