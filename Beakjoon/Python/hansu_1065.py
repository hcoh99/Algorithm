def hansu(num):
    if num < 100:
        return True
    elif 100 <= num <= 1000:
        hundred = num // 100
        ten = num % 100 // 10
        one = num % 10
        if hundred - ten == ten - one:
            return True
        else:
            return False


cnt = 0
number = int(input())
for i in range(1, number + 1):
    if hansu(i):
        cnt += 1

print(cnt)
