n = int(input())
a = list(map(int, input().split()))

for i in range(2000+1):
    if i not in a:
        print(i)
        exit()
