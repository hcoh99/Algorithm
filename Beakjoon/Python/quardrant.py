a = int(input())
b = int(input())
if a > 0 and b > 0:
    res = 1
elif a > 0 and b < 0:
    res = 4
elif a < 0 and b > 0:
    res = 2
elif a < 0 and b < 0:
    res = 3
print(res)
