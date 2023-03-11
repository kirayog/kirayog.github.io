s = list(input())

dic = {"a":0, "t":1, "c":2, "o":3, "d":4, "e":5, "r":6}
ansStr = "atcoder"
ans = 0

for i in range(len(s)-1):
    for j in range(len(s)-1):
       if dic[s[j]] > dic[s[j+1]]:
            tmp = s[j+1]
            s[j+1] = s[j]
            s[j] = tmp
            ans += 1
            
print(ans)
