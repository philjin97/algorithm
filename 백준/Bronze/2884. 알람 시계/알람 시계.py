(a, b) = list(map(int, input().split()))

if b < 45:
    if a == 0:
        a = 23
        b = 60 + (b - 45)
        print(a, b, sep=' ')

    elif a > 0:
        a -= 1
        b = 60 + (b - 45)
        print(a, b, sep=' ')
elif b >= 45:
    b -= 45 
    print(a, b, sep=' ')