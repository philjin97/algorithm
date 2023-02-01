import sys 

N = int(sys.stdin.readline())

while True:
    flag = True
    for a in str(N):
        if a != '4' and a != '7':
            flag = False
            N -= 1
    if flag:
        print(N)
        break