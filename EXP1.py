
from heapq import heappush, heappop

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    return sum(
        abs(i // 3 - (v - 1) // 3) +
        abs(i % 3 - (v - 1) % 3)
        for i, v in enumerate(state) if v
    )

def solve(start):
    pq = [(heuristic(start), 0, start, [])]
    visited = set()

    while pq:
        _, cost, state, path = heappop(pq)

        if state == goal:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        z = state.index(0)
        for move in (-3, 3, -1, 1):
            n = z + move
            if 0 <= n < 9 and not (
                move == -1 and z % 3 == 0 or
                move == 1 and z % 3 == 2
            ):
                new = list(state)
                new[z], new[n] = new[n], new[z]
                new = tuple(new)
                if new not in visited:
                    heappush(pq, (
                        cost + 1 + heuristic(new),
                        cost + 1, new, path + [state]
                    ))
    return None

start = tuple(map(int, input("Enter 9 numbers (0 for blank): ").split()))
result = solve(start)

if result:
    for state in result:
        print(state[:3], state[3:6], state[6:])
else:
    print("No solution found")