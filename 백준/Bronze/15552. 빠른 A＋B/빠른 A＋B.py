import sys

T = int(input())

for t in range( 1, T+1):
    (a, b) = (list(map(int, sys.stdin.readline().split())))
    print(a + b)