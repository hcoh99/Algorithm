import sys

a = int(sys.stdin.readline())
chc = []
for i in str(a):
    chc.append(i)
chc.sort(reverse=True)
b = 1
res = 0
for i in chc[::-1]:
    res += int(i) * b
    b *= 10
print(res)
