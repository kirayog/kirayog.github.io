import itertools

n, m = map(int, input().split())

c = list(itertools.combinations(range(1, m+1), n))

for i in range(len(c)):
    print(*c[i])
