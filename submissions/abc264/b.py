r, c = map(int, input().split())

array = [["" for _ in range(15)] for _ in range(15)]

for i in range(15):
    for j in range(15):
        for k in range(8):
            if array[i][j] == "" and (i==k or j==k or i==14-k or j==14-k):
                if k%2 == 0:
                    array[i][j] = "black"
                else:
                    array[i][j] = "white"

print(array[r-1][c-1])
