def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
ansArray = []
for i in range(n):
    for j in range(n):
        if i != j:
            ansArray.append(distance(array[i], array[j]))

print(max(ansArray))
