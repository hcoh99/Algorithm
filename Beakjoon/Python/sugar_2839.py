n = int(input())
rst = 0
while n >= 0:
    if n % 5 == 0:
        rst += n // 5
        break
    n -= 3
    rst += 1
    if n < 3:
        break
if n < 3 and n > 0:
    print(-1)
else:
    print(rst)
# 아이디어 및 사고의 흐름 적어 놓기.
