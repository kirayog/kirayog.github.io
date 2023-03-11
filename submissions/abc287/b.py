n, m = map(int, input().split())

nList = ["" for _ in range(n)]
mList = ["" for _ in range(m)]
ans = 0

for i in range(n):
    nList[i] = input()

for i in range(m):
    mList[i] = input()
    
for i in range(n):
    for j in range(m):
        if nList[i][3] == mList[j][0] and nList[i][4] == mList[j][1] and nList[i][5] == mList[j][2]:
            ans += 1
            break
            
print(ans)
