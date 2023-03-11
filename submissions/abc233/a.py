x, y = map(int, input().split())
if x > y:
    print("0")
else:
    if (y-x)%10 == 0: print((y-x)//10)
    else: print((y-x)//10 + 1)
