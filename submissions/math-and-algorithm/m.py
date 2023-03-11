import math

n = int(input())
array = [1]
newArray = []

for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        array.append(i)
        
for i in range(len(array)):
    print(array[i])
    print(n//array[i])
