import math

n = int(input())
sq = int(math.sqrt(n))+1
array = []

tmp = 2
while n != 1:
    if tmp > sq:
        array.append(n)
        break
    if n%tmp == 0:
        n = n//tmp
        array.append(tmp)
    else:
        tmp += 1

array.sort()
print(*array)
