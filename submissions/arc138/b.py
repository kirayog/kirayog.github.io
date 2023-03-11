n = int(input())
a = list(map(int, input().split()))

judge = 0
flag = False
sta = 0
end = n-1
while sta <= end:
    if a[end] == judge:
        end -= 1
    elif a[sta] == judge:
        sta += 1
        if judge == 0:
            judge = 1
        else:
            judge = 0
    else:
        flag = True
        break
if flag == True:
    print("No")
else:
    print("Yes")
