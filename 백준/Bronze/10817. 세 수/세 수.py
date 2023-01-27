import heapq

numbers = list(map(int, input().split()))

heapq.heapify(numbers)
heapq.heappop(numbers)
print(numbers[0])