t = int(input())


def make_binary(n):
    i = 1
    while i <= n:
        i *= 2
    i //= 2

    temp_n = n
    binary_lst = []
    while i >= 1:
        if temp_n - i >= 0:
            binary_lst.append(1)
            temp_n -= i
        else:
            binary_lst.append(0)
        i //= 2

    length = len(binary_lst)
    for idx in range(length - 1, -1, -1):
        if binary_lst[idx] == 1:
            print(length - idx - 1, end=' ')


for _ in range(t):
    n = int(input())
    make_binary(n)
