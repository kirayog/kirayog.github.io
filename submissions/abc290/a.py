n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0

for i in range(n):
    if i+1 in b:
        ans += a[i]
        
print(ans)
