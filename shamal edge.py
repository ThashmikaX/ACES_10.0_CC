from math import comb

def scamming_ways(t, test_cases):
    results = []
    for i in range(t):
        K, S, a, b = test_cases[i]
        ways = comb(K, S) * comb(S, a) * comb(S, b)
        results.append(ways)
    return results

t = 3
test_cases = [(11, 4, 2, 2), (25, 10, 6, 3), (20, 12, 4, 2)]
print(scamming_ways(t, test_cases))
