import sys
sys.setrecursionlimit(100000)

test_case_num = int(input())

drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]

answer = 0
answers = []


def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < m


def can_visit(r, c):
    if not in_range(r, c):
        return False
    if not grid[r][c]:
        return False
    if visited[r][c]:
        return False
    return True


def dfs(r, c):
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if can_visit(nr, nc):
            visited[nr][nc] = True
            dfs(nr, nc)


for _ in range(test_case_num):
    m, n, k = tuple(map(int, input().split()))

    grid = [
        [0] * m
        for _ in range(n)
    ]

    visited = [
        [False] * m
        for _ in range(n)
    ]

    for _ in range(k):
        c, r = tuple(map(int, input().split()))
        grid[r][c] = 1

    for i in range(n):
        for j in range(m):
            if grid[i][j] and not visited[i][j]:
                answer += 1
                dfs(i, j)

    answers.append(answer)
    answer = 0

for elem in answers:
    print(elem)
