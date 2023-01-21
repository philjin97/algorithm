chess_original= [1, 1, 2, 2, 2, 8]
chess_input = list(map(int, input().split()))
fix = []

for a in range(len(chess_original)):
    value = chess_original[a] - chess_input[a]
    fix.append(value)

for n in fix:
    print(n , end=' ')