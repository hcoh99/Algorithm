num = int(input())
check_list = []
# check_list.append(word[0])


def check(word):
    global check_list
    check_list.append(word[0])
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            continue
        else:
            if word[i] in check_list:
                return False
                break
            else:
                check_list.append(word[i])
    return True


cnt = 0
for _ in range(num):
    word = input()
    if check(word) == True:
        cnt += 1
    check_list.clear()

print(cnt)
