## <a href="https://school.programmers.co.kr/learn/courses/30/lessons/12944">평균 구하기</a>

### Solution (JavaScript)

- 풀이한 날짜 : 2022-12-12

<br/>

```js
// 풀이 1
function solution(arr) {
  let answer = 0;
  let sumOfNums = 0;

  arr.forEach((item) => {
    sumOfNums += item;
  });

  answer = sumOfNums / arr.length;

  return answer;
}
```

```js
// 풀이 2
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

- 배열의 모든 요소를 더해준 다음 배열의 길이로 나눠주면 된다.

- 두 번째 풀이는 <code>reduce</code> 배열 메소드를 활용한 풀이이다. (처음 알게 된 메소드)

<br/>

#### Feeling

- 쉬운 문제라도 여러 풀이가 있을 수 있음을 명심하고 더 좋은 풀이를 자주 보면서 공부해야겠다는 생각이 들었다.
