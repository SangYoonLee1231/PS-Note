lst = [
    int(input())
    for _ in range(9)
]

answer_lst = []


# a, b번째 난쟁이 제외하고 키 합 구하기
def get_sum(a, b):
    height_sum = 0
    for i in range(9):
        if i == a or i == b:
            continue
        height_sum += lst[i]
    return height_sum


# 정답 찾음 - a, b번째 난쟁이 제외한 나머지 난쟁이 키를 정답 리스트에 삽입
def make_answer_lst(a, b):
    for i in range(9):
        if i == a or i == b:
            continue
        answer_lst.append(lst[i])


def main_func():
    for i in range(9):
        for j in range(i + 1, 9):
            if i == j:
                continue
            # i, j번째 난쟁이 제외한 나머지 난쟁이 키 합이 100인지 확인
            if get_sum(i, j) == 100:
                make_answer_lst(i, j)
                return


main_func()
answer_lst.sort()
for elem in answer_lst:
    print(elem)
