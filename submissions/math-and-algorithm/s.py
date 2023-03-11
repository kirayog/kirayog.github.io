n = int(input())
a = list(map(int, input().split()))
array = [0 for _ in range(3)]
ans = 0

for i in range(n):
    array[a[i]-1] += 1

for i in range(3):
    ans += array[i] * (array[i]-1) // 2
    
print(ans)
