n, k, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    if k > a[i]//x:
        k -= a[i]//x
        a[i] = a[i]%x
    else:
        a[i] -= x*k
        k = 0
        break
        
a.sort()
a.reverse()
if k < n:
    print(sum(a[k:]))
else:
    print(0)
