## <a href="https://school.programmers.co.kr/learn/courses/30/lessons/120956">옹앓이 (1)</a>

### 풀이 (JavaScript)

- 풀이한 날짜 : 2022-12-20

<br/>

```js
function solution(babbling) {
  const correctBabbling = ["aya", "ye", "woo", "ma"];
  let count = 0;

  babbling.forEach((item) => {
    let oneBabble = item;
    for (let i = 0; i < correctBabbling.length; i++) {
      if (item.includes(correctBabbling[i])) {
        oneBabble = oneBabble.replace(correctBabbling[i], "");
      }
    }
    if (oneBabble === "") {
      count++;
    }
  });

  return count;
}
```

<br/>

#### 풀이 로직 및 문제 접근 과정

- babbling 배열의 요소를 하나하나씩 확인한다.

- 각 요소가 4개의 옹앓이 ["aya", "ye", "woo", "ma"] 의 조합으로 구성되어 있는지 확인한다.

- 이 때, 탐색중인 babbling 요소에 4개의 옹앓이가 있을 때마다 이를 빈 문자열로 대체한다.

- 만일 이렇게 할 경우, 4개의 옹앓이의 조합만으로 구성된 babbling 요소라면 결국 빈 문자열만 남게 될 것이다. 이렇게 되는 경우의 수를 세어주면 된다.

<br/>

#### 느낀점

- 부트캠프 동기 분 앞에서 (온라인이긴 했지만) 즉석으로 풀어본 문제.

- 생각보다 조건이 따질 것이 많아 진땀이 좀 났지만, 차분하게 생각한 덕분에 헤메지 않고 잘 풀어냈다.

<br/>
