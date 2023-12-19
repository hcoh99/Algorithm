word = input().upper()
dic = {}
result = []
for i in word:
    try:
        dic[i] += 1
    except:
        dic[i] = 1
for j, k in dic.items():
    if max(dic.values()) == k:
        result.append(j)
if len(result) > 1:
    print("?")
else:
    print(result[0])
