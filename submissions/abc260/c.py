def red(n):
    if n < 2:
        return 0
    else:
        return red(n-1) + blue(n)*x

def blue(n):
    if n < 2:
        return n
    else:
        return red(n-1) + blue(n-1)*y

n, x, y = map(int, input().split())

print(red(n))
