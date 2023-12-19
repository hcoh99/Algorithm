num = int(input())
# rst = 1
# for i in range(1, num + 1):
#     rst *= i
# print(rst)


def fac(n):
    if n > 0:
        return n * fac(n - 1)
    else:
        return 1


print(fac(num))
