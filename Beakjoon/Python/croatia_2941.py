word = input().lower()
# while i < len(word):
# if word[i] == "c" and word[i + 1] == "=":
#     cnt += 1
#     i += 2

# elif word[i] == "c" and word[i + 1] == "-":
#     cnt += 1
#     i += 2

# elif word[i] == "d" and word[i + 1] == "-":
#     cnt += 1
#     i += 2

# elif word[i] == "n" and word[i + 1] == "j":
#     cnt += 1
#     i += 2

# elif word[i] == "l" and word[i + 1] == "j":
#     cnt += 1
#     i += 2
# elif word[i] == "s" and word[i + 1] == "=":
#     cnt += 1
#     i += 2
# elif word[i] == "d" and word[i + 1] == "z" and word[i + 2] == "=":
#     cnt += 1
#     i += 3
# elif word[i] == "z" and word[i + 1] == "=":
#     cnt += 1
#     i += 2
# else:
#     cnt += 1
#     i += 1
ref = ["c-", "c=", "dz=", "z=", "lj", "nj", "s=", "d-"]
for i in ref:
    word = word.replace(i, "k")
print(len(word))
