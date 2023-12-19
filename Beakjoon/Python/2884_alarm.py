time = input()
h,m = map(int , time.split(' '))
if m < 45:
    n_m = (60-45)+m
    if h != 0:
        h = h - 1
    else: h = 23
    print(h , n_m)
elif m >= 45:
    n_m = m - 45
    print(h , n_m)
    