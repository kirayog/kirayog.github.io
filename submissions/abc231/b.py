n = int(input())
dic = {}

for i in range(n):
    s = input()
    if s in dic: dic[s] += 1
    else: dic[s] = 1
        
print(max(dic, key=dic.get))
