test = int(input())

for _ in range(test):
    p,q = list(map(int, input().split()))
    numberOfDruun = int(input())
    strength = list(map(int, input().split()))

    allSusuStre = p+q
    druunsStre = 0
    for i in range(numberOfDruun):
        druunsStre = druunsStre + strength[i]

    seconds = druunsStre // allSusuStre
    print(seconds)
