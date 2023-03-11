def f(a, b):
    if a % b == 0: return b
    else: return f(b, a%b)

n = int(input())
a = list(map(int, input().split()))
ans = a[0]

for i in range(1, n):
    ans = f(ans, a[i])
    
print(ans)
