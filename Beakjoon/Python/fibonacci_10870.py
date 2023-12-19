import sys

input = sys.stdin.readline
num = int(input())


def re(k):
    if k == 0:
        return 0
    elif k == 1:
        re(k - 1)
        return 1
    else:

        return re(k - 1) + re(k - 2)


print(re(num))
