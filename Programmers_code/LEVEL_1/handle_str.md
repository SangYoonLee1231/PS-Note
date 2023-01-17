## <a href="https://school.programmers.co.kr/learn/courses/30/lessons/12918">문자열 다루기 기본</a>

### Solution (JavaScript)

- 풀이한 날짜 : 2022-12-30

<br/>

```js
function solution(s) {
  let answer = true;

  if (s.length !== 4 && s.length !== 6) {
    answer = false;
  }

  if (isNaN(Number(s)) || s.includes("e")) {
    answer = false;
  }

  return answer;
}
```

<br/>

#### Logic

- answer 변수를 true로 초기화하고, 문제의 조건이 하나라도 만족하지 않을 경우 이 변수를 false로 할당해준다.

<br/>

#### Feeling

- <code>isNaN</code>이란 메서드를 처음으로 알게 해준 문제

  - <code>if ("a123" === NaN) { ... } </code> 이렇게 NaN인지를 판단하면 조건식이 false로 평가되므로 올바른 결과를 얻을 수 없다.

- 또한 <code>"10e1"</code>와 같은 지수 형태는 문자 <code>e</code>가 포함되어 있음에도 <code>NaN</code>형이 아닌 <strong>숫자형</strong>으로 평가된다는 것을 알 수 있었다.
