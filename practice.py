a, b = tuple(map(int, input().split()))

cnt = 0; ans = 0

def count():
    for i in range(1, 1001):
        for j in range(1, i+1):
            cnt += 1
            if a <= cnt and cnt <= b:
                ans += i
            if cnt > b:
                return

count()
print(ans)        