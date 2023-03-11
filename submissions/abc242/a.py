a, b, c, x = map(int, input().split())
ans = 0

if x <= a:
    ans = 1
elif a+1 <= x <= b:
    ans = c/(b-a)

print(ans)
