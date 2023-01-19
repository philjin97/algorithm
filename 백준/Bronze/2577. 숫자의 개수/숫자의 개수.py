A = int(input())
B = int(input())
C = int(input())

total = str(A*B*C)
numbers = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}

for n in total:
    numbers[n] += 1

for a in range(10):
    print(numbers[str(a)])