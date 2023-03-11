n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))

for i in range(q-p+1):
    tmp = a[p+i-1]
    a[p+i-1] = a[r+i-1]
    a[r+i-1] = tmp
    
print(*a)
