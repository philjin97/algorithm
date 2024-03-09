import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n = int(input())

def isPrime(num):
    for i in range(3, int(num/2 + 1)):
        if num % i == 0:
            return False
    return True
    
def dfs(x):
    if len(str(x)) == n:
        print(x)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if isPrime(10*x + i):
                dfs(10*x + i)
    
dfs(2)
dfs(3)
dfs(5)
dfs(7)