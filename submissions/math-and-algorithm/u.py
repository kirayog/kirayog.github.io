def f(n, r):
    if r == 0: return 1
    return n*f(n-1, r-1)

n, r = map(int, input().split())
print(f(n, r)//f(r, r))
