## <a href="https://school.programmers.co.kr/learn/courses/30/lessons/12916">문자열 내 p와 y의 개수</a>

### 풀이 (JavaScript)

- 풀이한 날짜 : 2022-12-16

<br/>

```js
function solution(s) {
  s = s.toLowerCase().split("");
  let [pCount, yCount] = [0, 0];

  s.forEach((item) => {
    if (item === "p") {
      pCount++;
    }
    if (item === "y") {
      yCount++;
    }
  });

  return pCount === yCount ? true : false;
}
```

<br/>

#### 풀이 로직 및 문제 접근 과정

- 문자열을 모두 소문자로 바꾸고 p의 개수와 q의 개수를 세서 비교한다.

<br/>

#### 느낀점

- 문제의 요구 사항에 따라 정직하게 풀면 답이 나오는 문제

<br/>
