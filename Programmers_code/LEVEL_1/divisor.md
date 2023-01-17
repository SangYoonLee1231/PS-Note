## <a href="https://school.programmers.co.kr/learn/courses/30/lessons/12928">약수의 합</a>

### Solution (JavaScript)

- 풀이한 날짜 : 2022-12-13

<br/>

```js
function solution(n) {
  let answer = 0;

  for (let i = 1; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      answer += i;
    }
  }

  return answer;
}
```

```js
function solution(arr) {
  return (
    arr.reduce((acc, cur, idx) => {
      acc += cur;
      return acc;
    }, 0) / arr.length
  );
}
```

<br/>

#### Logic

- n을 1부터 n까지 나눴을 때 나머지가 0인 수들을 모두 더해주면 된다.

<br/>

#### Feeling

- 처음에 문제를 풀 때 소수를 구하는 문제랑 헷갈려서 초기 조건으로 <code>n === 0</code>일 때와 <code>n === 1</code>일 때의 경우를 따로 처리했는데, 그럴 필요가 없었다. (아쉽)
