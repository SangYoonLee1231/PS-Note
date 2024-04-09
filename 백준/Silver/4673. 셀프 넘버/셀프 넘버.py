def func_d(num):
    answer = num
    num_str = str(num)

    for elem in num_str:
        answer += int(elem)

    return answer


numbers = [i for i in range(10001)]

for i in range(1, 10001):
    result = func_d(i)

    if result > 10000:
        continue

    numbers[result] = 0

for i in range(10001):
    if numbers[i] == 0:
        continue

    print(i)
