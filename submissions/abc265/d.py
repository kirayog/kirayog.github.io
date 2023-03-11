import bisect

n, p, q, R = map(int, input().split())
a = list(map(int, input().split()))

sumA = [0 for _ in range(n+1)]
sumA[0] = 0
sumA[1] = a[0]

for i in range(1, n):
    sumA[i+1] = sumA[i] + a[i]
    
for i in range(n+1):
    l = bisect.bisect_left(sumA,p+sumA[i])
    r = bisect.bisect_right(sumA,p+sumA[i])
    if l == r:
        continue
    left = l
    
    l = bisect.bisect_left(sumA,q+sumA[left])
    r = bisect.bisect_right(sumA,q+sumA[left])
    if l == r:
        continue
    left = l
        
    l = bisect.bisect_left(sumA,R+sumA[left])
    r = bisect.bisect_right(sumA,R+sumA[left])
    if l == r:
        continue
    left = l
    
    print("Yes")
    exit()
    
print("No")
