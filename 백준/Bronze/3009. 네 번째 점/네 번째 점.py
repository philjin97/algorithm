row = []
column = []

for n in range(3):
    (a, b) = list(map(int, input().split()))
    if a in row:
        row.remove(a)
        if b in column: 
            column.remove(b)
        else: 
            column.append(b)
    else:
        row.append(a)
        if b in column: 
            column.remove(b)
        else: 
            column.append(b)
    
print(row[0], column[0])