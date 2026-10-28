
graph = {}
n = int(input("Enter number of edges: "))

for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

start = input("Enter starting vertex: ")
visited = set()

def dfs(node):
    if node in visited:
        return

    visited.add(node)
    print(node, end=" ")

    for neighbor in graph.get(node, []):
        dfs(neighbor)

dfs(start)