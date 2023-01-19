number = int(input())
attendance = {}

for n in range(number):
    log = input().split()
    if log[0] not in attendance:
        attendance[log[0]] = log[1]
    else:
        attendance.pop(log[0])

attendance_order = sorted(list(attendance), reverse=True)

for a in attendance_order:
    print(a)