s = input()
array = []
tmpArray = []
alpha = [False for _ in range(1000)]
now = 0

for i in range(len(s)):
    if s[i] == "(":
        if len(array) > now:
            array.append(array[now] + tmpArray)
        else:
            array.append(tmpArray)
        tmpArray = []
        now += 1
    elif s[i] == ")":
        for j in range(len(tmpArray)):
            alpha[ord(tmpArray[j])] = False
        tmpArray = []
        if len(array) > now:
            for j in range(len(array[now])):
                alpha[ord(array[now][j])] = False
            array.pop()
        now -= 1
    else:
        if alpha[ord(s[i])] == True:
            print("No")
            exit()
        else:
            alpha[ord(s[i])] = True
        tmpArray.append(s[i])
        
print("Yes")
