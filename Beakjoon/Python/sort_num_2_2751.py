"""퀵정렬"""


# N = int(input())
# nums = [0 for i in range(N)]


# def qsort(a, left, right):
#     pl = left
#     pr = right
#     x = a[left + right // 2]
#     while pl <= pr:
#         while a[pl] < x:
#             pl += 1
#         while a[pr] > x:
#             pr -= 1
#         if pl <= pr:
#             a[pr], a[pl] = a[pl], a[pr]
#             pl += 1
#             pr -= 1
#     if left < pr:
#         qsort(nums, left, pr)
#     if right > pl:
#         qsort(nums, pl, right)


# for i in range(N):
#     a = int(input())
#     nums[i] = a
# qsort(nums, 0, N - 1)
# for i in nums:
#     print(i)

"""병합정렬"""

# n = int(input())
# a = []
# b = []
# c = [0 for _ in range(n)]
# for _ in range(0, n // 2):
#     a.append(int(input()))
# for _ in range((n // 2) + 1, n + 1):
#     b.append(int(input()))
#     a.sort()
#     b.sort()


# def merge_sort(a, b, c):
#     pa = pb = pc = 0
#     na, nb, nc = len(a), len(b), len(c)
#     while pa < na and pb < nb:
#         if a[pa] <= b[pb]:
#             c[pc] = a[pa]
#             pa += 1
#         else:
#             c[pc] = b[pb]
#             pb += 1
#         pc += 1
#     while pa < na:
#         c[pc] = a[pa]
#         pa += 1
#         pc += 1
#     while pb < nb:
#         c[pc] = b[pb]
#         pb += 1
#         pc += 1
#     return c


# for i in merge_sort(a, b, c):
#     print(i)

import sys

n = int(sys.stdin.readline())
b = []
for i in range(n):
    a = int(sys.stdin.readline())
    b.append(a)

for i in sorted(b):
    print(i)
