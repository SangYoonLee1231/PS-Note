s = int(input())
sum_of_nums = 0

i = 1
while sum_of_nums <= s:
    sum_of_nums += i
    i += 1

print(i - 2)

# i <=> s
# 1 <=> (1) = 1, 2
# 2 <=> (1+2) = 3, 4, 5
# 3 <=> (1+2+3) = 6, 7, 8, 9