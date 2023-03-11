n, k = map(int, input().split())
a = list(map(int, input().split()))
xy = []

ans = [-1 for _ in range(n)]

for i in range(n):
    xy.append(list(map(int, input().split())))

for i in range(k):
    for j in range(n):
        if ans[j] == -1:
            ans[j] = ((xy[a[i]-1][0]-xy[j][0])**2+(xy[a[i]-1][1]-xy[j][1])**2)**0.5
        else:
            ans[j] = min(ans[j], ((xy[a[i]-1][0]-xy[j][0])**2+(xy[a[i]-1][1]-xy[j][1])**2)**0.5)
            
print(max(ans))
