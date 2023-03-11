h, w = map(int, input().split())

array = []

for i in range(h):
    str = input()
    for j in range(w):
        if str[j] == "o":
            array.append([i, j])
            
ans = abs(array[0][0] - array[1][0]) + abs(array[0][1] - array[1][1])
print(ans)
