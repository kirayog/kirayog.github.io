s = input()
for i in range(len(s)):
    flag = True
    for j in range(len(s)):
        if i != j and s[i] == s[j]:
            flag = False
    if flag == True:
        print(s[i])
        exit()
print(-1)
