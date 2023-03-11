import math

n = int(input())

flag = True
for i in range(2, int(math.sqrt(n))+1):
  if n % i == 0:
    flag = False
    break
        
print("Yes" if flag else "No")
