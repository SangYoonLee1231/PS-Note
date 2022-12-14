## <a href="https://programmers.co.kr/learn/courses/30/lessons/12932">자연수 뒤집어 배열로 만들기</a>

### 풀이 (JavaScript)

- 풀이한 날짜 : 2022-12-14

<br/>

```js
function solution(n) {
  const strN = n.toString();
  let answer = [];

  for (let i = strN.length - 1; i >= 0; i--) {
    answer.push(Number(strN[i]));
  }

  return answer;
}
```

```js
function solution(n) {
  let answer = [];

  do {
    answer.push(n % 10);
    n = parseInt(n / 10);
  } while (n > 0);

  return answer;
}
```

<br/>

#### 풀이 로직 및 문제 접근 과정

- 자연수를 문자열로 만들고 뒤에서부터 answer 배열에 push한다.

- 다른 풀이로, 자연수를 10으로 나누었을 때의 나머지를 answer 배열에 push하고, 그 몫을 자연수로 업데이트 한다. 이 과정을 반복한다.

<br/><br/>
