n, a, b = map(int, input().split())

ans = 0

if n < a:
    ans = 0
elif a <= b:
    ans = n-a+1
else:
    ans = n//a*b
    if n%a < b:
        ans -= b-n%a-1

print(ans)
