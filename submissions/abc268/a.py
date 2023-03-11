a = list(map(int, input().split()))
dic = {}

for i in range(len(a)):
    dic[a[i]] = 0
    
print(len(dic))
