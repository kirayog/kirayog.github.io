n = int(input())
a = list(map(int, input().split()))

ans = 0
count = 0

for i in range(n):
    if i == a[i]-1:
        count += 1

for i in range(n):
    if i == a[i]-1:
        ans += count-1
    elif a[a[i]-1]-1 == i:
        ans += 1
        
print(ans//2)
