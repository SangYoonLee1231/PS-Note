## <a href="https://school.programmers.co.kr/learn/courses/30/lessons/140108">문자열 나누기</a>

### 풀이 (JavaScript)

- 풀이한 날짜 : 2023-01-08

<br/>

```js
// 1차 풀이
function solution(s) {
  let answer = 0;
  let [sameWithX, diffWithX] = [0, 0];
  let x = "";
  let flag = false;

  for (let i in s) {
    if (flag) {
      if (s[i] === x) {
        sameWithX++;
      } else {
        diffWithX++;
      }

      if (sameWithX === diffWithX) {
        answer++;
        [sameWithX, diffWithX] = [0, 0];
        flag = false;
      }
    } else {
      x = s[i];
      sameWithX++;
      flag = true;
    }
  }

  if (!(sameWithX === 0 && diffWithX === 0)) {
    answer++;
  }

  return answer;
}

s = "abracadabra";
console.log(solution(s));
```

```js
// 2차 풀이 (수정)
function solution(s) {
  let answer = 0;
  let countAboutX = 0;
  let x = "";
  let flag = false;

  for (let i in s) {
    if (countAboutX === 0) {
      answer++;
      x = s[i];
      countAboutX++;
    } else {
      if (s[i] === x) {
        countAboutX++;
      } else {
        countAboutX--;
      }
    }
  }

  return answer;
} 
```

<br/>

#### 문제 접근 과정

- 문자열을 처음부터 끝까지 딱 한 번만 순회하면서 주어진 조건에 맞춰 케이스를 분류하면 되니, (문자열을 순회하는) 반복문 내에 조건문을 잘 활용하면 답을 구할 수 있을 거라 생각했다.

- 처음에는 문제 조건에 따라 문자열을 나눌 때 코드 상에 입력받았던 문자열 s도 함께 분리하여 새 배열에 담을 지 고민했는데, 결국 나누진 않고 카운트만 세는 방향으로 문제를 해결했다.

  - 푸는 도중에 깨달았는데, 이렇게 풀면 문제에서 '두 횟수가 같아지는 순간' 뒤에 남은 문자열이 있을 경우, answer 값에 1을 추가로 더해주어야 한다.

<br/>

#### 느낀점

- Not Easy 했지만, '문자열 순회' + '케이스 분류'를 통해 30분에 걸쳐 풀어낸 문제

- 그러나 효율성이 높은 코드를 작성해서 풀진 않은 것 같아 좀 아쉬웠다.

- 다른 분의 깔끔한 풀이를 참고하니 이해가 어렴풋이 되긴 하는데, 내가 이걸 한 번에 코드로 쳐서 풀 수 있으려면 훨씬 더 많은 경험과 실력이 필요하겠구나 싶었다.

- 그래도 성장을 위해 다른 분의 코드를 계속 읽어보면서 내 코드에서 수정할 점을 찾아 다시 풀이를 작성해보았다. (2차 풀이)

<br/>
