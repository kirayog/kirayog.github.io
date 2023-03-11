q = int(input())

dic = {}
maxNum = -1
minNum = 10**9+1

for i in range(q):
    str = list(map(int, input().split()))
    if str[0] == 1:
        if str[1] in dic:
            dic[str[1]] += 1
        else:
            dic[str[1]] = 1
        maxNum = max(maxNum, str[1])
        minNum = min(minNum, str[1])
    elif str[0] == 2:
        if str[1] in dic:
            if dic[str[1]]-str[2] <= 0:
                dic.pop(str[1])
                if len(dic) > 0:
                    if str[1] == maxNum:
                        tmp = list(dic.keys())
                        maxNum = max(tmp)
                    if str[1] == minNum:
                        tmp = list(dic.keys())
                        minNum = min(tmp)
                else:
                    maxNum = -1
                    minNum = 10**9+1
            else:
                dic[str[1]] -= str[2]
    elif str[0] == 3:
        print(maxNum-minNum)
