(a, b) = list(map( int, input().split()))
seta = set(list(map(int, input().split())))
setb = set(list(map(int, input().split())))

print(len(seta - setb) + len(setb - seta))