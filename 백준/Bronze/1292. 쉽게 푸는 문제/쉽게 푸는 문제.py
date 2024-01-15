start, end = tuple(map(int, input().split()))
start, end = start - 1, end - 1
answer = 0

lst = [0] * 1000


def make_lst():
    idx = 0
    for i in range(1, 47):
        for _ in range(i):
            lst[idx] = i
            idx += 1
            if idx == 1000:
                return


make_lst()
for i in range(start, end + 1):
    answer += lst[i]

print(answer)
