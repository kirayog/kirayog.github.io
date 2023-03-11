n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

array = []

max = max(a)
for i in range(n):
    if a[i] == max:
        array.append(i)
        
for i in range(k):
    for j in range(len(array)):
        if b[i]-1 == array[j]:
            print("Yes")
            exit()
            
print("No")
