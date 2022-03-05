n = int(input())

lst_a = list(map(int, input().split()))
lst_b = list(map(int, input().split()))

lst_a.sort()

ans = 0
for elem in lst_a:
    max_in_b = max(lst_b)
    lst_b.pop(lst_b.index(max_in_b))

    ans += elem * max_in_b

print(ans)