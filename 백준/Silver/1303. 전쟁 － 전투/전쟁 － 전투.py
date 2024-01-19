c, r = tuple(map(int, input().split()))

grid = [
    list(input())
    for _ in range(r)
]

visited = [
    [False] * c
    for _ in range(r)
]

drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]

we_power = 0
enemy_power = 0

count = 0

# WE = White | ENEMY = Blue


def in_range(curr_r, curr_c):
    return curr_r >= 0 and curr_r < r and curr_c >= 0 and curr_c < c


def search(r, c):
    global count

    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and not visited[nr][nc] and grid[r][c] == grid[nr][nc]:
            visited[nr][nc] = True
            count += 1
            search(nr, nc)


for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            visited[i][j] = True
            count = 1
            search(i, j)

            if grid[i][j] == 'W':
                we_power += (count**2)
            else:
                enemy_power += (count**2)

print(we_power, enemy_power)
