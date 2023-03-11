n = int(input())
array = [0 for _ in range(n)]
ans = -1;

for i in range(n):
    array[i] = list(input())
    array[i] = list(map(int, array[i]))
    
for i in range(10):
    time = 0
    stop = [False for _ in range(n)]
    while True:
        for j in range(n):
            if i == array[j][time%10] and stop[j] == False:
                stop[j] = True
                break
        time += 1
        if False not in stop:
            break
    if ans != -1:
        ans = min(ans, time-1)
    else:
        ans = time-1
        
print(ans)
