s = input()

array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for i in range(len(array)):
    if array[i] == s:
        if i == 0:
            print(5)
        elif i == 1:
            print(4)
        elif i == 2:
            print(3)
        elif i == 3:
            print(2)
        elif i == 4:
            print(1)
        exit()
