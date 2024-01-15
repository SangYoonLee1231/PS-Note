import math

n = int(input())
lst = list(map(int, input().split()))
answer = 0


def check_prime_num(num):
    if num == 1:
        return False
    if num == 2:
        return True

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


for elem in lst:
    if check_prime_num(elem):
        answer += 1

print(answer)
