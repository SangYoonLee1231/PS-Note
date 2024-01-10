from collections import deque

n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input()))
    for _ in range(n)
]

dist_grid = [
    [0] * m
    for _ in range(n)
]
dist_grid[0][0] = 1

q = deque()

drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]


def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < m


def bfs():
    while q:
        r, c, num = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if in_range(nr, nc) and grid[nr][nc] and not dist_grid[nr][nc]:
                dist_grid[nr][nc] = num
                q.append((nr, nc, num + 1))


q.append((0, 0, 2))
bfs()

print(dist_grid[n - 1][m - 1])
