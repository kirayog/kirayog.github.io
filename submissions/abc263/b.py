n = int(input())
p = list(map(int, input().split()))

current = n-2
ans = 0

for i in range(n):
    if p[current] == 1:
        print(ans+1)
        exit()
    current = p[current]-2
    ans += 1
