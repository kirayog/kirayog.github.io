n = int(input())
a = list(map(int, input().split()))
array = [0 for _ in range(4)]

for i in range(n):
    array[a[i]//100-1] += 1
    
print(array[0]*array[3] + array[1]*array[2])
