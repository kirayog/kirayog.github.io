n, a, b = map(int, input().split())

ans = [[0 for _ in range(n*b)] for _ in range(n*a)]

for i in range(n*a):
    for j in range(n*b):
        if i//a%2 == 0 and j//b%2 == 0:
            ans[i][j] = "."
        elif i//a%2 == 1 and j//b%2 == 1:
            ans[i][j] = "."
        else:
            ans[i][j] = "#"

for i in range(len(ans)):
    print("".join(ans[i]))
