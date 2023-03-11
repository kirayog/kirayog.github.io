n = int(input())

array = list(map(int, format(n, 'b')))
array.reverse()
ansArray = []

for i in range(len(array)):
    array[i] = array[i]*(2**i)
    
for i in range(len(array)):
    if array[i] != 0:
        ansArray.append(array[i])
        
n = len(ansArray)
for i in range(2**n):
    ans = 0
    for j in range(n):
        if ((i >> j) & 1):
            ans += ansArray[j]
    print(ans)
