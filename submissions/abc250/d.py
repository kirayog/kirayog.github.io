def eratosthenes_sieve(n):
    is_prime = [True]*(n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, n + 1):
        if is_prime[p]:
            for q in range(2*p, n + 1, p):
                is_prime[q] = False
    return is_prime

n = int(input())
is_prime = eratosthenes_sieve(int(n**(1/3)//1))
ans = 0

for i in range(2, int(n**(1/3)//1+1)):
    if is_prime[i] == False:
        continue
    else:
        for j in range(2, i):
            if is_prime[j] == True:
                if j*i**3 <= n:
                    ans += 1
                else:
                    break
print(ans)
