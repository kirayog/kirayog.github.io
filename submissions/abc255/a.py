r, c = map(int, input().split())

array = []

for i in range(2):
    array.append(list(map(int, input().split())))
    
print(array[r-1][c-1])
