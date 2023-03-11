n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = []

count = 0
flag = False
tmp = []
for i in range(n):
    if count < m and i == a[count]-1:
        flag = True
        tmp.insert(0, i)
        count += 1
    elif flag == True:
        tmp.insert(0, i)
        for j in range(len(tmp)):
            ans.append(tmp[j]+1)
        tmp = []
        flag =False
    elif flag == False:
        ans.append(i+1)
        
print(*ans)
