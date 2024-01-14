import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

min_num = lst[0]; max_num = lst[0]

for i in range(n):
  if min_num > lst[i]: min_num = lst[i]
  if max_num < lst[i]: max_num = lst[i]

print(min_num, max_num)