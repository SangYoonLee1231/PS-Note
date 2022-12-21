## <a href="https://school.programmers.co.kr/learn/courses/30/lessons/12935">제일 작은 수 제거하기</a>

### 풀이 (JavaScript)

- 풀이한 날짜 : 2022-12-19

<br/>

```js
function solution(arr) {
  let [minNum, minNumIndex] = [arr[0], 0];

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < minNum) {
      minNum = arr[i];
      minNumIndex = i;
    }
  }

  arr.splice(minNumIndex, 1);
  return arr.length ? arr : [-1];
}
```

```js
function solution(arr) {
  const minNum = Math.min(...arr);
  const minNumIndex = arr.indexOf(minNum);

  arr.splice(minNumIndex, 1);
  return arr.length ? arr : [-1];
}
```

<br/>

#### 풀이 로직 및 문제 접근 과정

- 배열의 가장 작은 요소의 인덱스 값을 찾는다.

- 해당 요소를 제거한 새 배열을 반환한다.

  - 배열의 길이를 체크하여 만일 0일 경우 빈 배열 대신 [-1]를 반환해준다.

<br/>

#### 느낀점

- 문제의 요구 사항에 따라 정직하게 풀면 답이 나오는 문제

- 여러 메소드를 적재적소에 활용할 수 있도록 잘 익혀두어야겠다.

<br/>
