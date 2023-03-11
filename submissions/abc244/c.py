n = int(input())
array = [0 for _ in range(2*n+1)]

while True:
    for i in range(len(array)):
        if array[i] == 0:
            array[i] = 1
            print(i+1)
            break
    num = int(input())
    if num == 0:
        exit()
    array[num-1] = 1
