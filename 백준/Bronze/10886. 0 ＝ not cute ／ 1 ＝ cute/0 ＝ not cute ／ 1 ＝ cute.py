N = int(input())
cute = {'0': 0, '1': 0}

for n in range(N):
    person = input()
    if person in cute:
        cute[person] += 1

if cute['0'] > cute['1']:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
