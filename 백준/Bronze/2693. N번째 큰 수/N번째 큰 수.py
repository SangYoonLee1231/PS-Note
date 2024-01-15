test_case = int(input())

for _ in range(test_case):
    a = list(map(int, input().split()))

    a.sort()
    print(a[-3])
