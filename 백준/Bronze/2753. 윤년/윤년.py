year = int(input())

if year % 4 == 0:
    if year % 100 != 0:
        print('1')
    elif year % 400 == 0:
        print('1')
    else:
        print('0')
else:
    print('0')