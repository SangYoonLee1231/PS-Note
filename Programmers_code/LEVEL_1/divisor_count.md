## <a href="https://school.programmers.co.kr/learn/courses/30/lessons/77884">약수의 개수와 덧셈</a>

### 풀이 (JavaScript)

- 풀이한 날짜 : 2022-12-26

<br/>

```js
function solution(left, right) {
  let answer = 0;
  for (let i = left; i <= right; i++) {
    if (isDivisorCountEven(i)) {
      answer += i;
    } else {
      answer -= i;
    }
  }

  return answer;
}

function isDivisorCountEven(n) {
  let count = 0;
  for (let i = 1; i <= n; i++) {
    if (n % i === 0) {
      count++;
    }
  }

  return !(count % 2);
}
```

<br/>

#### 풀이 로직 및 문제 접근 과정

- left부터 right까지 각각의 수의 약수의 개수를 구한다.

  - 약수의 개수를 구하는 방법은 n(자기 자신의 수)을 1부터 n까지 나눠봤을 때 나머지가 0인 경우를 모두 세면 된다.

- 약수의 개수가 짝수인 수는 더하고, 홀수인 수는 빼서 그 결과를 답으로 반환한다.

<br/>

#### 느낀점

- 주어진 조건에 맞춰 정직하게 푸니 쉽게 풀렸던 문제

- 함수 사용이 매우 NICE 했다.

<br/>

- '어떤 수의 제곱근이 정수라면 그 수의 약수의 개수는 홀수'라는 수학적 성질을 이용하면 더 쉽게 풀 수 있는 문제임을 다른 사람의 풀이를 통해 알 수 있었다.

- 비록 이런 기발한 아이디어가 생각이 나지 않더라도 이번 문제는 시키는 대로만 계산한다면 쉽게 풀리는 문제였다. 하지만 이런 발상을 하는 것이 안 중요하다곤 말할 순 없으니, 이렇게 짚고 넘어간다.

<br/>
