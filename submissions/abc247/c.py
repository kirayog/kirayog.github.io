memo = {}

def f(x):
    if x == 1:
        return 1
    if x in memo:
        return memo[x]
    ans = str(f(x-1)) + " " + str(x) + " " + str(f(x-1))
    memo[x] = ans
    return ans

n = int(input())
print(f(n))
