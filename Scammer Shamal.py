import math

def count_scam_ways(K, S, a, b):

    newbies = K-S
    number = newbies
    B1 = math.comb(number, a)
    number = number - a
    B2 = math.comb(number, b)
    number = number - b
    B3 = math.comb(number, (newbies - a - b))

    result = B1*B2*B3
    return result

# Read input and solve each test case
T = int(input())
for _ in range(T):
    ksab = list(map(int, input().split()))
    result = count_scam_ways(ksab[0], ksab[1], ksab[2], ksab[3])
    print(result)
