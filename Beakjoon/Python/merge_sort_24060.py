def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    i = p
    j = q + 1
    t = 1
    tmp = [None] * r
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            tmp[t] = A[j]
            t += 1
            j += 1
    while i <= q:
        tmp[t] = A[i]
        t += 1
        i = 1
    while j <= r:
        tmp[t] = A[j]
        t += 1
        j += 1
    i = p
    t = 1
    while i <= r:
        A[i] = tmp[t]
        i += 1
        t += 1
    return A


n = int(input())
lis = list(map(int, input().split()))
print(merge_sort(lis, 0, len(lis)))
