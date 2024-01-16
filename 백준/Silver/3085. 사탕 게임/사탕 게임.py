n = int(input())

grid = [
    list(input())
    for _ in range(n)
]

max_candies = 0


def check_line():
    global max_candies

    for i in range(n):
        temp = 1
        max_temp = 1

        for j in range(n - 1):
            if grid[i][j] == grid[i][j + 1]:
                temp += 1
                max_temp = max(max_temp, temp)
            else:
                temp = 1

        max_candies = max(max_candies, max_temp)

    for i in range(n):
        temp = 1
        max_temp = 1

        for j in range(n - 1):
            if grid[j][i] == grid[j + 1][i]:
                temp += 1
                max_temp = max(max_temp, temp)
            else:
                temp = 1

        max_candies = max(max_candies, max_temp)


def change_candies():
    for i in range(n):
        for j in range(n - 1):
            grid[i][j], grid[i][j + 1] = grid[i][j + 1], grid[i][j]
            check_line()
            grid[i][j], grid[i][j + 1] = grid[i][j + 1], grid[i][j]

    for i in range(n - 1):
        for j in range(n):
            grid[i][j], grid[i + 1][j] = grid[i + 1][j], grid[i][j]
            check_line()
            grid[i][j], grid[i + 1][j] = grid[i + 1][j], grid[i][j]


change_candies()
print(max_candies)
