import math

L, R = map(int, input().split())

for i in range(R-L):
    for j in range(i+1):
        if math.gcd(L+j, R-i+j) == 1:
            print(R-L-i)
            exit()
