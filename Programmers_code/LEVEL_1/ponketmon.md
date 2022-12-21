## <a href="https://school.programmers.co.kr/learn/courses/30/lessons/1845">폰켓몬</a>

### 풀이 (JavaScript)

- 풀이한 날짜 : 2022-12-21

<br/>

```js
function solution(nums) {
  let noJungbokNums = [];
  nums.forEach((item, index) => {
    if (!noJungbokNums.includes(item)) {
      noJungbokNums.push(item);
    }
  });

  return Math.min(noJungbokNums.length, nums.length / 2);
}
```

```js
function solution(nums) {
  let noJungbookNums = [...new Set(nums)];

  return noJungbookNums.length > nums.length / 2
    ? nums.length / 2
    : noJungbookNums.length;
}
```

<br/>

#### 풀이 로직 및 문제 접근 과정

- n개 중 n/2개만을 선택하여 가장 많은 종류의 폰켓몬을 뽑아야한다.

- 그렇다면 어떻게든 최대한 많은 종류의 폰켓몬을 고른다 하더라도 가능한 경우의 최댓값은 n/2개이다. 이는 폰켓몬의 종류가 n/2개 이상일 때만 성립한다.

- 만일 폰켓몬의 종류가 n/2개 미만일 경우 답은 폰켓몬의 종류의 수(n/2 미만인 수)가 된다.

- 즉, (폰켓몬의 종류의 수), (n/2) 이 둘 중 더 작은 값이 답이다.

<br/>

- 입력으로 주어진 nums 배열의 중복을 제거하여 (폰켓몬의 종류의 수)를 구할 수 있고, nums 배열의 길이를 2로 나누어 (n/2)를 구할 수 있다.

<br/>

#### 느낀점

- 문제를 어떻게 풀어야 할 지 로직을 잘 세우는 것이 정말 중요했던 문제

  - (솔직히 코드를 제출하기 전까지 풀이에 대한 확신은 없었다.)

- 문제를 주어진 조건에 따라 정직하게 풀어야 할 때도 있고 처음부터 풀이 설계를 잘 해야하는 문제도 있구나.

<br/>
