import sys
sys.setrecursionlimit(100000)

r, c, k = tuple(map(int, input().split()))

trash_grid = [
    [0] * c
    for _ in range(r)
]

visited = [
    [False] * c
    for _ in range(r)
]

count = 1
answer = 0

drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]

for _ in range(k):
    i, j = tuple(map(int, input().split()))
    i, j = i - 1, j - 1
    trash_grid[i][j] = 1


def in_range(curr_r, curr_c):
    return curr_r >= 0 and curr_r < r and curr_c >= 0 and curr_c < c


def search(r, c):
    global count

    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and not visited[nr][nc] and trash_grid[nr][nc]:
            visited[nr][nc] = True
            count += 1
            search(nr, nc)


for i in range(r):
    for j in range(c):
        if not visited[i][j] and trash_grid[i][j]:
            count = 1
            visited[i][j] = True
            search(i, j)
            answer = max(answer, count)

print(answer)
