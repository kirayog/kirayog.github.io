x1, y1, x2, y2 = map(int, input().split())
direction = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
Array1 = [[x1+direction[i][0], y1+direction[i][1]] for i in range(8)]
Array2 = [[x2+direction[i][0], y2+direction[i][1]] for i in range(8)]
for i in range(8):
    if Array1[i] in Array2:
        print("Yes")
        exit()
print("No")
