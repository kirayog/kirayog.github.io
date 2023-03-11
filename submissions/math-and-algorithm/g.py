import math

n, x, y = map(int, input().split())
print(n//x + n//y - n//(x*y // math.gcd(x, y)))
