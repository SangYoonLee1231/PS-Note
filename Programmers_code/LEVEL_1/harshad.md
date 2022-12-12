## <a href="https://programmers.co.kr/learn/courses/30/lessons/12947">하샤드 수</a>

### 풀이 1 (Python)

- 풀이한 날짜 : 2022-04-07

<br/>

```python
def solution(x):
    answer = True
    sum_x = 0
    str_x = str(x)
    for elem in str_x:
        sum_x += int(elem)

    if x % sum_x:
        answer = False

    return answer
```

<br/>

#### 풀이 로직 및 문제 접근 과정

- 결국 내가 하면 되는 것은 <code>x % (x의 각 자리수의 합) == 0</code> 이 참인가 거짓인가를 밝히는 것 뿐이다. (<code>O(1)</code> 시간 내에 충분히 가능)

- 그럼 관건은 'x의 각 자리수를 어떻게 분리해서 모두 더할 것인가' 인데,

- 이건 그냥 x를 문자열로 바꾸면, for문을 통해 x의 각 자리를 다 탐색할 수 있게 되므로 변수 하나 선언해서 모두 더해주면 된다.

  - 물론 더할 때 다시 정수로 형변환 해주어야 한다.

<br/>

#### 느낀점

- 어떻게 풀 지 1분 고민하고 바로 해결한 문제.

- 생각보다 프로그래머스 LEVEL 1 문제가 할 만하다는 것을 느끼고 자신감이 붙었다.

<br/><br/>

### 풀이 2 (Python) (모범 답안 참고)

<br/>

```python
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))
```

#### 풀이 로직

- 풀이 로직은 내 첫 풀이와 동일하다. (그럼에도 단 한 줄로만 짰다는 것이 대단한 거지..)

<br/>

#### 느낀 점

- list comprehension을 이용해서 이렇게 한 줄로 짤 수도 있구나.. 싶었다.

- <code>sum([int(c) for c in str(n)])</code> ← 이 표현식에 배울 점이 많다.

  - list comprehension과 sum 함수를 통해 '각 자리수의 합' 한 번에 계산하기
