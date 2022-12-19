## <a href="https://school.programmers.co.kr/learn/courses/30/lessons/12943">콜라츠 추측</a>

### Solution (JavaScript)

- 풀이한 날짜 : 2022-12-19

<br/>

```js
// 풀이 1: 반복문 사용
function solution(num) {
  if (num === 1) {
    return 0;
  }

  for (let i = 1; i <= 500; i++) {
    if (num % 2 === 0) {
      num /= 2;
    } else {
      num = num * 3 + 1;
    }
    if (num === 1) {
      return i;
    }
  }

  return -1;
}
```

```js
// 풀이 2: 재귀함수 사용
function solution(num) {
  return collatzCount(num, 1);
}

function collatzCount(num, acc) {
  if (num === 1) {
    return 0;
  }
  if (acc === 500) {
    return -1;
  }

  if (num % 2 === 0) {
    num /= 2;
  } else {
    num = num * 3 + 1;
  }

  return num === 1 ? acc : collatzCount(num, acc + 1);
}
```

<br/>

#### Logic

- 문제의 조건애 맞게 케이스를 나누어 계산하고 반복문을 사용하여 답을 구한다.

- (풀이 2) 반복문 대신 재귀함수를 사용해도 된다

<br/>

#### Feeling

- 바로 로직을 생각해서 풀었다. 다만 맨 처음에 예외 케이스를 빠뜨려서 틀렸다. (문제 잘 읽기!!)

- 다른 사람들의 풀이를 보고 재귀함수를 사용하여 다시 풀어봤다. 재귀함수도 내가 자유자재로 사용할 수 있는 도구가 빨리 되었음 좋겠다.
