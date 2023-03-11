a, b = map(int, input().split())

ans = (a**2 + b**2)**0.5
print(*[a/ans, b/ans])
