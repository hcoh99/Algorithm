import sys

input = sys.stdin.readline
num = int(input())
tmp = []


def convert(n, str):
    global tmp
    for i in str:
        for _ in range(int(n)):
            tmp.append(i)
    return tmp


for _ in range(num):
    nn, st = input().split()
    res = convert(nn, st)
    for i in res[::1]:
        print(i, end="")
    print(" ")
    res.clear()
