scores = [(a, sum(list(map(int, input().split())))) for a in range(1, 6)]

scores = sorted(scores, key = lambda x:x[1], reverse=True)

print(*scores[0])