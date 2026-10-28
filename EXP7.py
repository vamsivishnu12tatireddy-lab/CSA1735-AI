
from collections import deque

graph = {}
n = int(input("Enter number of edges: "))

for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

start = input("Enter starting vertex: ")
queue = deque([start])
visited = {start}

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)