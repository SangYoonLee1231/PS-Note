a, b = tuple(map(int, input().split()))


def find_gcd(a, b):
    if a > b:
        large = a
        small = b
    else:
        large = b
        small = a
    gcd_nom = 0

    for i in range(1, small + 1):
        if large % i == 0 and small % i == 0:
            gcd_nom = i
            gcd_nom = max(gcd_nom, i)
    return gcd_nom


def find_lcm(a, b, gcd):
    return a * b // gcd


gcd = find_gcd(a, b)
print(gcd)
print(find_lcm(a, b, gcd))
