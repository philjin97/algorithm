number = input()        
if len(number) == 1:
    number = '0' + number
    a = '0'
else: 
    a = number[0]
b = number[-1]
result = ''
cnt = 0

while number != result:
    added = int(a) + int(b)
    string = str(added)
    a = b
    b = string[-1]
    result = a + b
    cnt += 1

print(cnt)
