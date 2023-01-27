string = input()

if string == '고무오리 디버깅 시작':
    problem = []
    while True:
        direction = input()
        if direction == '문제':
            problem.append('문제')
        elif direction == '고무오리':
            if len(problem) > 0:
                problem.pop()
            else:
                problem.append('문제')
                problem.append('문제')
        elif direction == '고무오리 디버깅 끝':
            break
    if len(problem) == 0:
        print('고무오리야 사랑해')
    else:
        print('힝구')