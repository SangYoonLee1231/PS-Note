import math

def check(row, col, brown):
    return (row + col - 2) * 2 == brown


def solution(brown, yellow):
    # brown + yellow = row * col
    # brown = (row + col - 2) * 2
    
    for i in range(2, int(math.sqrt(brown + yellow)) + 1):
        if (brown + yellow) % i == 0:
            if check((brown + yellow) // i, i, brown):
                return [(brown + yellow) // i, i]