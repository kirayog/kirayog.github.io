n = int(input())

array = [[1]]

for i in range(1, n):
    tmpArray = []
    for j in range(i+1):
        if j == 0 or j == i:
            tmpArray.append(1)
        else:
            tmpArray.append(array[i-1][j-1] + array[i-1][j])
    array.append(tmpArray)
    
for i in range(n):
    print(*array[i])
    
