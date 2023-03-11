n, m, t = map(int, input().split())
a = list(map(int, input().split()))

dic = {}

for i in range(m):
    x, y = map(int, input().split())
    dic[x] = y
    
for i in range(n-1):
    if t > a[i]:
        t -= a[i]
        if i+2 in dic:
            t += dic[i+2]
    else:
        print("No")
        exit()
        
print("Yes")
