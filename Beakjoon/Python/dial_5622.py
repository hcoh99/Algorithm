dial = {
    "ABC": 2,
    "DEF": 3,
    "GHI": 4,
    "JKL": 5,
    "MNO": 6,
    "PQRS": 7,
    "TUV": 8,
    "WXYZ": 9,
}
word = input().upper()
mid = []
for i in range(len(word)):
    for k in dial.keys():
        if word[i] in k:
            mid.append(dial[k])
rst = sum(mid) + len(mid)
print(rst)
