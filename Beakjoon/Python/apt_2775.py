T = int(input())

for _ in range(T):
    floor = int(input())
    room = int(input())
    chart = [[i for i in range(1, room + 1)] for k in range(floor + 1)]
    k = 1
    n = 1
    while floor >= k:
        if room > 1:
            chart[k][0] = 1
            chart[k][n] = sum(chart[k - 1][0 : n + 1])
            n += 1
            if n == room:
                k += 1
                n = 1
        else:
            chart[k][0] = 1
            k += 1
    print(chart[floor][room - 1])
