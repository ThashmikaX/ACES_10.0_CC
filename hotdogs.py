import math

def are_coprime(a, b):
    gcd = math.gcd(a, b)
    return gcd == 1


dishescount = int(input())
diarray = list(map(int, input().split()))
ciarray = list(map(int, input().split()))

usedcindex = []*len(ciarray)
useddindex = []*len(diarray)

can_unlock_dishes = 0
for i in range(len(diarray)):
    for j in range(len(ciarray)):
        if are_coprime(diarray[i], ciarray[j]) == False:
            if i not in useddindex:
                if j not in usedcindex:
                    can_unlock_dishes+=1
                    usedcindex.append(j)
                    useddindex.append(i)

print(can_unlock_dishes)
