n = int(input())
p = list(map(int, input().split()))

array = [0 for i in range(n)]

for i in range(n):
    array[(p[i]-i+1)%n] += 1
    array[(p[i]-i)%n] += 1
    array[(p[i]-i-1)%n] += 1
    
print(max(array))
