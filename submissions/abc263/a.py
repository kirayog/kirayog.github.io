array = list(map(int, input().split()))
array.sort()

if array[0] == array[1] == array[2] and array[3] == array[4] and array[2] != array[3]:
    print("Yes")
elif array[0] == array[1] and array[2] == array[3] == array[4] and array[1] != array[2]:
    print("Yes")
else:
    print("No")
