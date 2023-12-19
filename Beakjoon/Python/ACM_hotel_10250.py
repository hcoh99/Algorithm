num = int(input())

for _ in range(num):
    H, W, N = map(int, input().split())
    if N % H == 0:
        Y = H
        X = N // H

    else:
        Y = N % H

        X = (N // H) + 1
    print(Y * 100 + X)
