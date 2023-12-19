cnt = 0

assem = []


def move(n, fm, to):
    global assem
    if n > 1:
        move(n - 1, fm, 6 - fm - to)

    assem.append([fm, to])

    if n > 1:
        move(n - 1, 6 - fm - to, to)
    return assem


n = int(input())
a = move(n, 1, 3)
print(len(a))
for i in a:
    print(*i)
