n, k = tuple(map(int, input().split()))


def check_div(cnt):
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
        if cnt == k:
            return i
    return 0


print(check_div(0))
