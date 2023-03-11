n, m = map(int, input().split())
nList = [[] for _ in range(n)]
 
for i in range(m):
    a, b = map(int, input().split())
    nList[a-1].append(b)
    nList[b-1].append(a)
    
for i in range(n):
    if len(nList[i]) == 0:
        print(0)
    else:
        nList[i].sort()
        print(len(nList[i]), *nList[i])
        
