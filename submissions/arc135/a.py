def f(a):
    if a in memo:
        return memo[a]
    else:
        memo[a] = f(a//2) * f((a+1)//2) % mod
        return memo[a]

x = int(input())
mod = 998244353
memo = {1:1, 2:2, 3:3, 4:4}

print(f(x))
