
from collections import deque

start = (3, 3, 1)
goal = (0, 0, 0)
moves = [(1, 0), (2, 0), (0, 1),
         (0, 2), (1, 1)]

def valid(m, c):
    return (0 <= m <= 3 and 0 <= c <= 3 and
            (m == 0 or m >= c) and
            (3-m == 0 or 3-m >= 3-c))

q = deque([(start, [start])])
visited = {start}

while q:
    state, path = q.popleft()
    m, c, boat = state

    if state == goal:
        for step in path:
            print(step)
        break

    for dm, dc in moves:
        direction = -1 if boat == 1 else 1
        nm = m + direction * dm
        nc = c + direction * dc
        nxt = (nm, nc, 1-boat)

        if dm + dc <= 2 and valid(nm, nc) and nxt not in visited:
            visited.add(nxt)
            q.append((nxt, path + [nxt]))