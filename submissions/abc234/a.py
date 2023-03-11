def f(t):
    return t**2 + 2*t + 3

t = int(input())
print(f(f(f(t)+t)+f(f(t))))
