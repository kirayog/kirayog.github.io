n, a, b = map(int, input().split())
s = input()

ans = -1

for i in range(n):
    count = a * i
    array = s[i:] + s[:i]
    for j in range(n//2):
        if array[j] != array[-j-1]:
            count += b
    if ans > count or ans == -1:
        ans = count
        
print(ans)
