import sys

input = sys.stdin.readline
num = int(input())
res_list = []
for _ in range(num):
    word = input().split()
    if word[0] == "push":
        res_list.append(word[1])
    elif word[0] == "pop":
        if len(res_list) > 0:
            print(res_list[-1])
            del res_list[-1]
        else:
            print(-1)
    elif word[0] == "size":
        print(len(res_list))
    elif word[0] == "empty":
        if len(res_list) == 0:
            print(1)
        else:
            print(0)
    elif word[0] == "top":
        if (len(res_list) > 0) == True:
            print(res_list[-1])
        else:
            print(-1)


### sys의 stdin.readline을 사용했을때의 효과와 언제 사용해야 하는지에 대해서 정리하기
