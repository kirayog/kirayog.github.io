n = int(input())
list = list(map(int, input().split()))
sumList = [360]

total = 0
for i in range(n):
    total += list[i]
    sumList.append(total%360)
sumList.sort()

maxRange = 0
preValue = 0
for value in sumList:
    maxRange = max(maxRange, value-preValue)
    preValue = value

print(maxRange)
