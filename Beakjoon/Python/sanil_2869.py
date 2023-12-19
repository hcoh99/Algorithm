import math

a, b, v = map(int, input().split())
# suum = 0
# cnt = 0
# while suum < v:
#     cnt += 1
#     suum += a
#     if suum >= v:
#         break
#     suum -= b

# print(cnt)
day = (v - b) / (a - b)

print(math.ceil(day))

# 왜 소수점이 나오면 올림을 해야아는지, 올림 및 내림,반노림 노션에 정리하기.
