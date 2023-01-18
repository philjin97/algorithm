sentence = input()

for n in range(len(sentence)):
    if (n + 1) % 10 == 0 and n != 0:
        print(sentence[n])
    else:
        print(sentence[n], end='')