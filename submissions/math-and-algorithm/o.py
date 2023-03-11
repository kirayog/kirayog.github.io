def f(a, b):
    if a % b == 0: return b
    else: return f(b, a%b)

a, b = map(int, input().split())

print(f(a, b))
