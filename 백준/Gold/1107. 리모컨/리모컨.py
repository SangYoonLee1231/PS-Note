# 다른 풀이 : 브루트포스
target = int(input())
btn_errors = int(input())

if btn_errors:
    error_btn_lst = list(map(int, input().split()))
else:
    error_btn_lst = []

target_lst = list(str(target))
min_cnt = abs(100 - target)


def check_valid(n):
    lst = map(int, list(str(n)))
    for elem in lst:
        if elem in error_btn_lst:
            return False
    return True


for i in range(1000001):
    if not check_valid(i):
        continue
    min_cnt = min(min_cnt, abs(i - target) + len(str(i)))

print(min_cnt)
