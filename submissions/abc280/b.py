n = int(input())
s = list(map(int, input().split()))

sum = 0
ans = [0 for _ in range(n)]

for i in range(n):
    ans[i] = s[i] - sum
    sum = s[i]
    
print(*ans)
