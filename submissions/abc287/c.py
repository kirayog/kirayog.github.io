n, m = map(int, input().split())

pList = [[] for _ in range(n)]
usedList = [False for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    pList[u-1].append(v-1)
    pList[v-1].append(u-1)
    
if n - m != 1:
    print("No")
    exit()
    
start = -1
end = -1

for i in range(n):
    if len(pList[i]) != 2:
        if len(pList[i]) == 1:
            if start == -1:
                start = i
                usedList[i] = True
            elif end == -1:
                end = i
            else:
                print("No")
                exit()
        else:
            print("No")
            exit()

if start == -1 or end == -1:
    print("No")
    exit()
    
for i in range(n-1):
    if i != 0 and i != n-2:
        if len(pList[start]) != 2:
            print("No")
            exit()
    if usedList[pList[start][0]] == False:
        start = pList[start][0]
        usedList[start] = True
    elif usedList[pList[start][1]] == False:
        start = pList[start][1]
        usedList[start] = True
    else:
        print("No")
        exit()
    
print("Yes")
