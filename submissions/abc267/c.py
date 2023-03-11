n, m = map(int, input().split())
a = list(map(int, input().split()))

array = [-1 for _ in range(n-m+1)]

total = 0
tmp = 0
for i in range(m):
    total += a[i]*(i+1)
    tmp += a[i]
array[0] = total

for i in range(1, n-m+1):
    total -= tmp
    total += a[i+m-1]*m
    tmp -= a[i-1]
    tmp += a[i+m-1]
    
    array[i] = total
    
print(max(array))
