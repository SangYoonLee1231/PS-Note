n = int(input())

for i in range(1, n + 1):
    a, b = tuple(map(int, input().split()))

    answer = (a + b) % 24

    print(f"#{i} {answer}")
