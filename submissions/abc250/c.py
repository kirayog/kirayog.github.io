n, q = map(int, input().split())

place = [i for i in range(n)]
ans = [i for i in range(n)]

for i in range(q):
    x = int(input())-1
    if place[x]+1 != n:
        tmp = ans[place[x]]
        ans[place[x]] = ans[place[x]+1]
        ans[place[x]+1] = tmp
        place[ans[place[x]]] -=1
        place[x] += 1
    else:
        tmp = ans[place[x]]
        ans[place[x]] = ans[place[x]-1]
        ans[place[x]-1] = tmp
        place[ans[place[x]]] +=1
        place[x] -= 1

for i in range(n):
    ans[i] += 1
print(*ans)
    
    
