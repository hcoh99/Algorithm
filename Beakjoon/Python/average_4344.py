import sys
import decimal

input = sys.stdin.readline
tot_num = int(input())


def get_avg(scores):
    avg = float(0)
    plus = float(0)
    for i in scores[1::]:
        plus += i
    avg = plus // scores[0]
    return avg


cnt = 0
for _ in range(tot_num):
    scores = list(map(int, input().strip().split()))
    k = get_avg(scores)

    for i in scores[1::]:
        if i > k:
            cnt += 1
    res = decimal.Decimal((cnt / scores[0]) * 100)
    cnt = 0
    print(f"{round(res,3)}%")

    # 부도ㅇ소수점 내용 정리하기
