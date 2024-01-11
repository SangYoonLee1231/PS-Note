input_str = input()
answer = 0

# 1st. 수식 문자열을 항으로 분류하여 리스트로 만듦
exp_lst = []

number = [i for i in range(10)]
number_temp = []
for elem in input_str:
    if elem in str(number):
        number_temp.append(elem)
    else:
        exp_lst.append(''.join(map(str, number_temp)))
        number_temp.clear()
        exp_lst.append(elem)
exp_lst.append(''.join(map(str, number_temp)))


# 2nd. 계산
minus_flag = False
temp_sum = 0

for idx, elem in enumerate(exp_lst):
    if idx == len(exp_lst) - 1:
        temp_sum += int(elem)
        if minus_flag == True:
            answer -= temp_sum
        else:
            answer += temp_sum

    if elem == '+':
        pass
    elif elem == '-':
        if minus_flag == False:
            minus_flag = True
            answer += temp_sum
        else:
            answer -= temp_sum
        temp_sum = 0
    else:
        temp_sum += int(elem)

print(answer)
