place = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

dxs = [0, 1, 1, 1, 0, -1, -1, -1]
dys = [1, 1, 0, -1, -1, -1, 0, 1]

king, stone, n = tuple(input().split())
n = int(n)

king_x = place.index(king[0]) + 1
king_y = int(king[1])

stone_x = place.index(stone[0]) + 1
stone_y = int(stone[1])

mapper = {
    'T' : 0,
    'RT' : 1,
    'R' : 2,
    'RB' : 3,
    'B' : 4,
    'LB' : 5,
    'L' : 6,
    'LT' : 7
}

def in_range(x, y):
    return x >= 1 and x <= 8 and y >= 1 and y <= 8

def move(dir_num):
    global king_x, king_y, stone_x, stone_y

    king_nx = king_x + dxs[dir_num]
    king_ny = king_y + dys[dir_num]

    if in_range(king_nx, king_ny):
        king_x = king_nx
        king_y = king_ny
    else:
        return

    if king_x == stone_x and king_y == stone_y:
        stone_nx = stone_x + dxs[dir_num]
        stone_ny = stone_y + dys[dir_num]

        if not in_range(stone_nx, stone_ny):
            king_x = king_x - dxs[dir_num]
            king_y = king_y - dys[dir_num]
        else:
            stone_x = stone_nx
            stone_y = stone_ny


for _ in range(n):
    direction = input()
    dir_num = mapper[direction]
    move(dir_num)

# 출력
king_x = place[king_x - 1]
print(king_x + str(king_y))

stone_x = place[stone_x - 1]
print(stone_x + str(stone_y))