## <a href="https://programmers.co.kr/learn/courses/30/lessons/12950">행렬의 덧셈</a>

### 풀이 (JavaScript)

- 풀이한 날짜 : 2023-01-18

<br/>

```js
function solution(arr1, arr2) {
  const row = arr1.length;
  const col = arr1[0].length;

  const answer = new Array();
  for (let i = 0; i < row; i++) {
    answer.push(new Array(col));
  }

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      answer[i][j] = arr1[i][j] + arr2[i][j];
    }
  }

  return answer;
}
```

<br/>

#### 느낀 점

- 자바스크립트에서 이차원 배열을 선언하는 방법을 여전히 헷갈려해서 시간이 소요됐던 문제였다.

- <code>new Array</code>의 쓰임을 좀 더 확실히 알고 넘어가자.

  ```js
  const answer = new Array();
  for (let i = 0; i < row; i++) {
    answer.push(new Array(col));
  }
  ```

<br/><br/>
