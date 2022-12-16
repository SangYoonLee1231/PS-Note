## <a href="https://school.programmers.co.kr/learn/courses/30/lessons/12934">정수 제곱근 판별</a>

### 풀이 (JavaScript)

- 풀이한 날짜 : 2022-12-16

<br/>

```js
function solution(n) {
  const x = Math.sqrt(n);

  if (Number.isInteger(x)) {
    return (x + 1) * (x + 1);
  } else return -1;
}
```

<br/>

#### 풀이 로직 및 문제 접근 과정

- n의 제곱근을 <code>Math.sqrt(n)</code>를 통해 구한다.

- 구한 n의 제곱근이 정수인지 실수인지 판별한다.

  - n이 양의 정수 x의 제곱이라면 이 값은 정수이고, 그렇지 않으면 이 값은 실수이다.

<br/>

#### 느낀점

- 메소드를 잘 활용해야 했던 문제.

<br/>
