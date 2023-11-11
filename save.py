from functools import reduce
def min_time_to_defeat_monsters(t, test_cases):
    results = []

    for i in range(t):
        p, q, n, strengths = test_cases[i]
        count = 0
        sum = reduce(lambda x, y: x + y, strengths)
        while (True):
            if p > q and sum > 0:
                sum -= p
                print("sumup", sum)
                p -= p
                p += p
                q += q

                count += 1
                print("A", count)

            elif p < q and sum > 0:
                sum -= q
                print("sumdown", sum)
                q-=q
                q+=q
                p+=p
                count += 1

                print("B", count)

            if sum < 0 or sum == 0:
                break

    results.append(count)


    return results

# Input
t = int(input())  # Number of test cases
test_cases = []

for _ in range(t):
    p, q = map(int, input().split())
    n = int(input())
    strengths = list(map(int, input().split()))
    test_cases.append((p, q, n, strengths))

# Calculate and print the results
results = min_time_to_defeat_monsters(t, test_cases)
for result in results:
    print(result)