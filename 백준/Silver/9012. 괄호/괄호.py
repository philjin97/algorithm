T = int(input())


for t in range(1, T+1):
    result = 0
    string = str(input())
    for a in string:
        if a == '(':
            result += 1
        elif a == ')': 
            result -= 1
            if result < 0:
                break
    if result == 0:
        print('YES')
    else:
        print('NO')