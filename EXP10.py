
import heapq

graph = {}
n = int(input("Enter number of edges: "))

for _ in range(n):
    u, v, cost = input("Enter edge (u v cost): ").split()
    cost = int(cost)
    graph.setdefault(u, []).append((v, cost))
    graph.setdefault(v, []).append((u, cost))

nodes = set(graph)
for edges in graph.values():
    for v, _ in edges:
        nodes.add(v)

h = {}
for node in sorted(nodes):
    h[node] = int(input(f"Heuristic for {node}: "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

pq = [(h[start], 0, start, [start])]
best = {start: 0}

while pq:
    _, g, node, path = heapq.heappop(pq)

    if node == goal:
        print("Path:", " -> ".join(path))
        print("Total cost:", g)
        break

    if g != best[node]:
        continue

    for neighbor, cost in graph.get(node, []):
        new_cost = g + cost

        if new_cost < best.get(neighbor, float("inf")):
            best[neighbor] = new_cost
            heapq.heappush(
                pq,
                (new_cost + h[neighbor], new_cost,
                 neighbor, path + [neighbor])
            )
else:
    print("No path found")