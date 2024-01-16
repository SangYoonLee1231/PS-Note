import sys

n = int(input())
num_lst = list(map(int, input().split()))
plus, minus, mul, div = tuple(map(int, input().split()))

operations_lst = ['+', '-', '*', '/']
exp_lst = []
exp_count = [0, 0, 0, 0]

min_result = sys.maxsize
max_result = -sys.maxsize


def calc():
    temp_lst = []
    temp = 0

    for elem in exp_lst:
        temp_lst.append(elem)

        if len(temp_lst) == 3:
            if temp_lst[1] == '+':
                temp = temp_lst[0] + temp_lst[2]
            elif temp_lst[1] == '-':
                temp = temp_lst[0] - temp_lst[2]
            elif temp_lst[1] == '*':
                temp = temp_lst[0] * temp_lst[2]
            elif temp_lst[1] == '/':
                temp = int(temp_lst[0] / temp_lst[2])

            temp_lst.clear()
            temp_lst.append(temp)

    return temp_lst[0]


def dfs(curr_num):
    global max_result, min_result

    if exp_count[0] > plus or exp_count[1] > minus or exp_count[2] > mul or exp_count[3] > div:
        return

    if curr_num == n - 1:
        result = calc()
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    for idx, elem in enumerate(operations_lst):
        exp_lst.append(elem)
        exp_lst.append(num_lst[curr_num + 1])
        exp_count[idx] += 1

        dfs(curr_num + 1)

        exp_lst.pop()
        exp_lst.pop()
        exp_count[idx] -= 1


exp_lst.append(num_lst[0])
dfs(0)

print(max_result)
print(min_result)
