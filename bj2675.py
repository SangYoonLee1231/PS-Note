from sys import stdin,stdout
input = stdin.readline
print = stdout.write

n = int(input())

for _ in range(n):
    repeat_num = int(input())
    input_str = list(input())    # list를 input 앞에 붙이면 입력받은 문자열을 글자로 잘라서 list로 저장한다.
