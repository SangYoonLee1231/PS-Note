## <a href="https://programmers.co.kr/learn/courses/30/lessons/49993">스킬트리</a>

### 풀이 1

- 풀이한 날짜 : 2022-04-06

<br/>

```python
def check(skill, skill_tree):
    pos = -1
    for skill_tree_elem in skill_tree:
        if skill_tree_elem in skill:
            for i, skill_elem in enumerate(skill):
                if skill_tree_elem == skill_elem:
                    if i == pos + 1:
                        pos = i
                        break
                    else:
                        return 0
    return 1

                    
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        answer += check(skill, skill_tree)

    return answer
```

#### 풀이 로직

- skill_trees의 각 skill_tree에 주어진 skill의 스킬(요소)들이 있을 경우, 이들이 skill의 나열 순서를 만족하는지 확인한다. (<code>check</code> 함수로 구현)

    - 이를 위해, skill_tree의 각 스킬 요소를 순서대로 탐색하면서, 이 스킬이 skiil에 있는 요소인지 우선 확인한다.

    - 만일 있을경우, 이 요소가 skill의 몇 번쨰 요소인지 확인한다.

    - 처음으로 skill에 있는 요소는 skill의 첫번째여야 하고, 그 다음은 두번쨰여야 한다.

    - 이런 식으로 일일이 확인했을 때 잘못된 경우가 없으면, 올바른 skill_tree라는 뜻이다. (1을 반환, 아니면 0을 반환)

- 답을 뜻하는 answer 변수의 초깃값을 0으로 설정하고, <code>check</code> 함수의 리턴값을 이 변수에 더해준다.

    - 문제의 조건을 만족하는 skill_tree 수만큼 <code>check</code> 함수의 리턴값을 answer 값에 더한다.

<br/>

#### 문제 접근 과정 및 느낀점

- 처음에 문제를 잘못 이해해서, 잘못된 풀이 로직을 바탕으로 코드를 작성했다.

    - <strong>입출력의 설명을 꼼꼼히 읽지 않아</strong> 저지른 실수였다. 앞으로 이 부분도 신경써야겠다.

    - 또한, 문제의 조건이 많을수록 이를 빠르고 정확하게 파악하는 연습을 앞으로 많이 해야할 필요성을 느꼈다. (<strong>문제 풀이 경험 ↑</strong>)

- 계속 중첩되는 for문과 if문으로 인해 가독성이 떨어진 코드를 작성했다. 이로 인해 문제 풀이도 더 지체된 것 같다.

    - 구체적인 대안은 잘 생각나진 않지만, 구현 능력을 더 키워야 하겠다는 생각은 확실히 든다.

        - 다시 한 번 살펴보니, 문제 이해 부족이 원인인 듯 하다. <strong>문제 꼼꼼히 읽고 충분히 생각하면서 알고리즘을 짜자.</strong>

<br/><br/>

### 풀이 2 (모범 답안 참고)

<br/>

```python
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
```

#### 풀이 로직

- <code>for-else</code>문

- list 활용, <code>pop</code> 함수 활용

<br/>

#### 느낀 점

- 👍

- 코드를 이렇게 작성할 수도 있구나.. 잘 배워갑니다. (특히 <code>pop</code> 함수 활용)