test = int(input())

for _ in range(test):
    string1, string2 = input().split()
    firstW = 0
    secondW = 0
    for i in range(len(string1)):
        if string1[i] == 'S':
            firstW+=2
        elif string1[i] == 'T':
            firstW += 4

    for i in range(len(string2)):
        if string2[i] == 'S':
            secondW+=2
        elif string2[i] == 'T':
            secondW += 4

    if firstW == secondW:
        print("True")
    else:
        print("False")