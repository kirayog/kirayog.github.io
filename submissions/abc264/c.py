import itertools

h1, w1 = map(int, input().split())
array1 = [[0 for _ in range(w1)] for _ in range(h1)]
for i in range(h1):
    array1[i] = list(map(int, input().split()))
    
h2, w2 = map(int, input().split())
array2 = [[0 for _ in range(w2)] for _ in range(h2)]
for i in range(h2):
    array2[i] = list(map(int, input().split()))
    
c1 = list(itertools.combinations(range(h1), h2))
c2 = list(itertools.combinations(range(w1), w2))

for i in range(len(c1)):
    for j in range(len(c2)):
        flag = True
        for k in range(h2):
            for l in range(w2):
                if array2[k][l] != array1[c1[i][k]][c2[j][l]]:
                    flag = False
                    break
        if flag == True:
            print("Yes")
            exit()
print("No")
