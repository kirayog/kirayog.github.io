n = int(input())
ans = []

for i in range(2, n+1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag == True:
        ans.append(i)
        
print(*ans)
