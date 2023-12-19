import sys

num1, num2 = sys.stdin.readline().split()


def conv(num):
    nnum = int(num[2]) * 100 + int(num[1]) * 10 + int(num[0])
    return nnum


A = conv(num1)
B = conv(num2)
if A < B:
    print(B)
else:
    print(A)
while i <= q:
    tmp[t] = A[i]
    t += 1
    i += 1
while j <= r:
    tmp[t] = A[j]
    t += 1
    j += 1
i = p
t = 1
while i <= r:
    A[i]
