n = int(input())
array = []

for i in range(n):
    array.append(input())
    
for i in range(n):
    print(array[n-i-1])
