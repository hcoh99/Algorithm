import sys

n = int(sys.stdin.readline())
count = [0 for _ in range(10001)]
for _ in range(n):
    count[int(sys.stdin.readline())] += 1
for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)
## 이러한 방식도 있다라는것을 알아 놓기.
