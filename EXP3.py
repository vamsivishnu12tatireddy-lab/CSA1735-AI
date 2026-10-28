
from collections import deque

def water_jug(a, b, target):
    q = deque([(0, 0, [])])
    visited = set()

    while q:
        x, y, path = q.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))
        path = path + [(x, y)]

        if x == target or y == target:
            return path

        states = [
            (a, y), (x, b), (0, y), (x, 0),
            (x - min(x, b - y), y + min(x, b - y)),
            (x + min(y, a - x), y - min(y, a - x))
        ]

        for state in states:
            if state not in visited:
                q.append((*state, path))

    return None

a = int(input("Capacity of jug 1: "))
b = int(input("Capacity of jug 2: "))
target = int(input("Target quantity: "))

result = water_jug(a, b, target)
print("Steps:", result if result else "No solution")