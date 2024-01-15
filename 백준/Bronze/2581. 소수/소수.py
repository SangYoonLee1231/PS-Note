import math

m = int(input())
n = int(int(input()))
prime_min = 10001
prime_sum = 0


def check_prime_num(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


for i in range(m, n + 1):
    if check_prime_num(i):
        prime_min = min(prime_min, i)
        prime_sum += i

if prime_min == 10001:
    print(-1)
else:
    print(prime_sum)
    print(prime_min)
