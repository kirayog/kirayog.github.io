s = input()
count = 0
flag = False

for i in range(len(s)):
    if s[i] == "0":
        if flag == False:
            flag = True
            count += 1
        else:
            flag = False
    else:
        flag = False
        count += 1

print(count)
