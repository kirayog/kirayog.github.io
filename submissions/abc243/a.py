v, a, b, c = map(int, input().split())

while True:
    if v < a:
        print("F")
        exit()
    v -= a
    if v < b:
        print("M")
        exit()
    v -= b
    if v < c:
        print("T")
        exit()
    v -= c
