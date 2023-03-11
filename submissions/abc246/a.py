x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
ansX, ansY = 0, 0

if x1 == x2:
    ansX = x3
elif x2 == x3:
    ansX = x1
else:
    ansX = x2

if y1 == y2:
    ansY = y3
elif y2 == y3:
    ansY = y1
else:
    ansY = y2
    
print(*[ansX, ansY])
