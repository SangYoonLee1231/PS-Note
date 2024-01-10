# # Sol 1. 완전 탐색 (O(2^n * n))
# n, goal_r, goal_c = tuple(map(int, input().split()))

# curr_state = [0 for i in range(n - 1)]

# curr_num = 0

# base_coord = {
#     0: (0, 0),
#     1: (0, 1),
#     2: (1, 0),
#     3: (1, 1),
# }


# def calc_coord():
#     r, c = 0, 0

#     for i in range(0, n - 1):
#         weight = 2 ** (i + 1)
#         dr, dc = base_coord[curr_state[i]]
#         r, c = r + (dr * weight), c + (dc * weight)

#     return r, c


# def backtrack(curr_n):
#     global curr_num

#     if curr_n == 0:
#         for i in range(4):
#             r, c = calc_coord()
#             dr, dc = base_coord[i]
#             r, c = r + dr, c + dc

#             if r == goal_r and c == goal_c:
#                 print(curr_num)
#                 exit(0)

#             curr_num += 1

#         return

#     for i in range(4):
#         curr_state[curr_n - 1] = i
#         backtrack(curr_n - 1)


# backtrack(n - 1)


# Sol 2. 일부만 탐색
import sys
sys.setrecursionlimit(100000)

n, r, c = tuple(map(int, input().split()))

grid_n = 2 ** n

high_bound = 0
low_bound = 0


def divide(grid_n, start_r, start_c, start_num):
    global high_bound, low_bound

    total_num = grid_n ** 2

    # 초기 조건
    if r == start_r and c == start_c:
        print(low_bound)
        exit(0)

    if r >= start_r and r < start_r + (grid_n // 2) and c >= start_c and c < start_c + (grid_n // 2):
        # 제 2사분면
        low_bound = start_num
        high_bound = start_num + (total_num // 4) - 1
        divide(grid_n // 2, start_r, start_c, low_bound)

    elif r >= start_r and r < start_r + (grid_n // 2) and c >= start_c + (grid_n // 2) and c < start_c + grid_n:
        # 제 1사분면
        low_bound = start_num + (total_num // 4)
        high_bound = start_num + (total_num // 2) - 1
        divide(grid_n // 2, start_r, start_c + grid_n // 2, low_bound)

    elif r >= start_r + (grid_n // 2) and r < start_r + grid_n and c >= start_c and c < start_c + (grid_n // 2):
        # 제 3사분면
        low_bound = start_num + (total_num // 2)
        high_bound = start_num + ((total_num // 4) * 3) - 1
        divide(grid_n // 2, start_r + grid_n // 2, start_c, low_bound)

    else:
        # 제 4사분면
        low_bound = start_num + ((total_num // 4) * 3)
        high_bound = start_num + total_num - 1
        divide(grid_n // 2, start_r + grid_n // 2,
               start_c + grid_n // 2, low_bound)


divide(grid_n, 0, 0, 0)
