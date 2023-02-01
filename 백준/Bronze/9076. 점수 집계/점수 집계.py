T = int(input())

for t in range(1, T+1):
    score = sorted(list(map(int, input().split())))
    three_score = [score[num] for num in range(1, 4)]
    if three_score[-1] - three_score[0] >= 4:
        print('KIN')
    else:
        print(sum(three_score))