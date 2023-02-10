import sys

INT_MIN = -sys.maxsize

n = 5
dp = [0] * n
a = [2, 3, 0, 1, 4]


def initalize():
    for i in range(n):
        dp[i] = INT_MIN
    dp[0] = 0

initalize()

for i in range(1, n):
    for j in range(n):
        if dp[i] == INT_MIN:
            continue

        if j + a[j] >= i:
            dp[i] = max(dp[i], dp[j] + 1)

ans = 0
for i in range(n):
    ans = max(ans, dp[i])

print(ans)
            