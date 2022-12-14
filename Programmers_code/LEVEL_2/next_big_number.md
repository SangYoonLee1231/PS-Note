## <a href="https://programmers.co.kr/learn/courses/30/lessons/12911">다음 큰 숫자</a>

### 풀이 (JavaScript)

- 풀이한 날짜 : 2022-12-14

<br/>

```js
function solution(n) {
  let numberOfOneInN = 0;
  n.toString(2)
    .split("")
    .forEach((item) => {
      if (item === "1") {
        numberOfOneInN++;
      }
    });

  let i = 1;
  while (true) {
    let numberOfOneInNextN = 0;
    (n + i)
      .toString(2)
      .split("")
      .forEach((item) => {
        if (item === "1") {
          numberOfOneInNextN++;
        }
      });

    if (numberOfOneInN === numberOfOneInNextN) {
      return n + i;
    }

    i++;
  }
}
```

#### 풀이 로직

- 자연수 n을 이진수로 바꾸고 1의 개수를 센다.

- n의 다음 수부터 순서대로 탐색하면서 이진수의 1의 개수가 n일 때와 같은 자연수를 찾는다.

<br/>

#### 느낀점

- 이진수를 코드로 다뤄본 경험이 별로 없어 처음에 조금 막막했으나, 검색을 통해 <code>.toString(2)</code>을 알고 난 후로는 수월했다.
