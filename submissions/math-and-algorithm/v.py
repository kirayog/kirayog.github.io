def f(n, r):
    if r == 0: return 1
    return n*f(n-1, r-1)

n = int(input())
a = list(map(int, input().split()))
array = [0 for _ in range(100000)]
ans = 0

for i in range(n):
    array[a[i]] += 1
    
for i in range(1, 50000):
    ans += array[i] * array[100000-i]

ans += f(array[50000], 2)//f(2, 2)
    
print(ans)
