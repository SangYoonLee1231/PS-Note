## <a href="https://programmers.co.kr/learn/courses/30/lessons/12938">최댓값과 최솟값</a>

### 풀이 (JavaScript)

- 풀이한 날짜 : 2022-12-14

<br/>

```js
function solution(s) {
  let nums = s.split(" ");
  nums = nums.map((item) => Number(item));

  let [minNum, maxNum] = [nums[0], nums[0]];

  for (let i = 1; i < nums.length; i++) {
    if (minNum > nums[i]) {
      minNum = nums[i];
    }
    if (maxNum < nums[i]) {
      maxNum = nums[i];
    }
  }

  return `${minNum} ${maxNum}`;
}
```

<br/>

#### 풀이 로직

- 문자열로 입력된 수열을 배열로 바꾸고, 최댓값, 최솟값을 찾는 로직을 적용한다.

  - 최솟값 찾는 로직 : 모든 원소를 순차적으로 탐색해서 현재 최솟값보다 더 작은 값이 있으면, 그 값으로 업데이트 한다. (최댓값 찾기도 같은 논리)

<br/>

#### 느낀점

- 일부러 내장 메소드를 쓰지 않고 최댓값, 최솟값 찾기를 직접 하드코딩 했다. (별로 길진 않았지만)
