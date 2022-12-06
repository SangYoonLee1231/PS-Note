# 파이썬 PS 입출력 팁

<br/>

## 나누어 입력받기

- 2개의 입력값이 다음처럼 주어졌을 때 각각의 변수에 값을 저장하는 방법

```
10 25
```

```python
a, b  = map(int, input().split())

c = list(map(int, input(),split()))
# c에 두 입력값을 리스트(list)로 저장
```

<br/>

## 입력 출력 가속

- 입출력 가속함수로 입력과 출력을 빠르게 받을 수 있다.

- 일반적인 코딩테스트에선 안 써도 무방하지만, 백준 문제에선 입출력 가속함수를 써야 시간 초과를 피할 수 있는 경우가 있다.  
  (백준 1927번, 백준 10845번)

```python
import sys
N = int(sys.stdin.readline())
sys.stdout.write(N)
```

- 그러나 매번 입출력마다 저렇게 쓰는 것은 시간적인 측면에서 손해이므로..

```python
from sys import stdin, stdout
input = stdin.readline
print = stdout.write
```

- 코드 맨 위에 다음을 작성하고 평소처럼 <code>print()</code>, <code>input()</code> 함수를 쓰면 된다.

<br/>

## 문자열을 한 글자씩 잘라서 저장하기

- 문자열을 한 글자씩 잘라서 저장하고 싶으면 <code>list(input())</code>으로 입력받으면 된다.

```
apple
```

▲ 입력 값

```python
lst = list(input())
```

▲ Code

```
['a', 'p', 'p', 'l', 'e']
```

▲ 출력 값
