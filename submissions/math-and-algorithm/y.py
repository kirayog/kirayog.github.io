n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0

for i in range(n):
    ans += a[i]/3 + b[i]*2/3
    
print(ans)
