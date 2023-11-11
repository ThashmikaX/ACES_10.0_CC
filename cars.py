
cars_in_single = int(input())
n = cars_in_single*cars_in_single
total_races = 0

if n > 3:
    total_races = cars_in_single + 1

print(total_races)
