x, y, n = map(int, input().split())

if x*3 < y:
    print(x*n)
else:
    print(n//3*y + n%3*x)
