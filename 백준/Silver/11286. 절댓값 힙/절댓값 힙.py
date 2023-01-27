import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for num in range(n):
    number = int(sys.stdin.readline())
    if number == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(number), number))