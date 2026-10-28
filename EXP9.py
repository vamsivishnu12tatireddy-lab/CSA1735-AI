
from itertools import permutations

n = int(input("Enter number of cities: "))
cost = []

print("Enter cost matrix:")
for i in range(n):
    cost.append(list(map(int, input().split())))

best_cost = float("inf")
best_path = None

for p in permutations(range(1, n)):
    path = (0,) + p + (0,)
    total = sum(cost[path[i]][path[i+1]]
                for i in range(n))

    if total < best_cost:
        best_cost = total
        best_path = path

print("Shortest path:", " -> ".join(
    chr(65 + city) for city in best_path
))
print("Minimum cost:", best_cost)