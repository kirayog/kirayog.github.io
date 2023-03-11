x, a, d, n = map(int, input().split())

if d == 0:
    print(abs(x-a))
    exit()

if d < 0:
    a = a + d * (n-1)
    d = -d #d‚ð³‚É‚·‚é
first = x-a #a‚ð0‚ÉŒÅ’è
ans1 = 0
ans2 = 0

if first < 0:
    ans1 = abs(x-a)
    ans2 = abs(x-a)
else:
    numberItem = first//d
    if numberItem > n-1:
        numberItem = n-1
        print(abs(x-(a + d * numberItem)))
        exit()
    elif numberItem < 0:
        numberItem = 0
        print(abs(x-(a + d * (numberItem+1))))
        exit()
    ans1 = abs(x-(a + d * numberItem))
    ans2 = abs(x-(a + d * (numberItem+1)))
    
print(min(ans1, ans2))


    
