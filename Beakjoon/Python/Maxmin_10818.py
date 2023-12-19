import sys

input = sys.stdin.readline
num = int(input())

num_list = list(map(int, input().strip().split()))
max = num_list[0]
min = num_list[0]
for i in range(1, num):
    if num_list[i] > max:
        max = num_list[i]
    if num_list[i] < min:
        min = num_list[i]

print(min, max)
