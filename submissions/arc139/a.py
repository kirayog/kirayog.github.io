n = int(input())
t = list(map(int, input().split()))

ans = 0

for i in range(n):
    count = 0
    while True:
        if (ans >> t[i]+count) & 1:
            count += 1
        else:
            break
    ans = ans >> t[i]+count
    ans = ans << t[i]+count
    ans += 2**(t[i]+count)
    if (ans >> t[i]) & 1 == 0:
        ans += 2**t[i]

print(ans)
