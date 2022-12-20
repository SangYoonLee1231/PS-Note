## <a href="https://school.programmers.co.kr/learn/courses/30/lessons/138477">명예의 전당 (1)</a>

### 풀이 (JavaScript)

- 풀이한 날짜 : 2022-12-20

<br/>

```js
function solution(k, score) {
  let scoresRank = [];
  let answer = [];

  for (let i = 1; i <= score.length; i++) {
    scoresRank.push(score[i - 1]);
    let rankIndex = -1;

    // scoresRank 오름차순 정렬
    scoresRank.sort((a, b) => a - b);

    if (k < i) {
      rankIndex = i - k;
    } else {
      rankIndex = 0;
    }

    let announcedScore = scoresRank[rankIndex];
    answer.push(announcedScore);
  }

  return answer;
}
```

<br/>

#### 풀이 로직 및 문제 접근 과정

<풀이 Key Point>

- 첫날부터 k일까지의 발표 점수는 전체 꼴등 점수이다.

- 하지만 k+1일부터의 발표 점수는 전체의 k등 점수이다.

  - 예시 k = 4일 경우, 1~4일차 : 전테 꼴등, 5일차~ : 전체 4등

<풀이 방법>

- 임시 배열을 하나 만들어(scoresRank) 그날의 점수를 하나씩 추가하고, 날마다 이 배열을 오름차순으로 정렬한다.

- 발표 점수에 해당하는 등수의 점수를 이 배열에서 인덱스 값을 이용해 뽑아 answer 배열에 push한다.

<br/>

#### 느낀점

- Lv. 1의 정답률이 낮은 문제를 일부러 골러서 한 번 풀어봤는데, 역시 문제를 이해하는 것도, 로직도 쉽진 않았지만 그래도 할 만했다.

- 오히려 생각보다 빠르게 답을 맞춰 조금 놀랐다.

- 문제를 잘 파악하고 코드 작성 전 미리 풀이를 잘 설계해두면 이 정도 수준의 문제들은 웬만큼 다 풀 수 있겠구나.

<br/>
