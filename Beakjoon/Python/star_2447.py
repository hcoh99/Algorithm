def stars(n):
    matrix = []
    for i in range(3 * len(n)):  # 최소 9 이드부터 들어오기 떄문에... 3곱해줌
        if i // 3 == 1:  # 빈칸은 자기자신으로 나누었을떄, 1이면 생긴다 그치만 이것은 그 줄의 전체저포맷을 전부 챙겨준것,,,,
            (
                matrix.append(n[i % len(n)])
                + " " * len(n)
                + matrix.append(n[i % len(n)])
            )  # 빈칸 앞쪽에는 원래 들어와야것들이...
        else:
            matrix.append(n[i % len(n)])  # n의 순서대로 들어온다.
            return list(matrix)


star = ["***", "* *", "***"]
k = 0
num = int(input())
while num != 3:  # 3의 몇배수인지를 구하는 과정...
    num = int(num / 3)
    k += 1

for i in range(k):
    star = stars(star)
for i in star:
    print(i)
