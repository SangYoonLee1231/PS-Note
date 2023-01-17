## <a href="https://school.programmers.co.kr/learn/courses/30/lessons/82612">부족한 금액 계산하기</a>

### Solution (JavaScript)

- 풀이한 날짜 : 2022-12-30

<br/>

```js
function solution(price, money, count) {
  let cost = 0;

  for (let i = 1; i <= count; i++) {
    cost += i;
  }
  cost *= price;

  return cost - money > 0 ? cost - money : 0;
}
```

<br/>

#### Logic

- answer 변수를 true로 초기화하고, 문제의 조건이 하나라도 만족하지 않을 경우 이 변수를 false로 할당해준다.

<br/>

#### Feeling

- JavaScript에선 <code>-1</code>과 같은 음수도 <code>truthy</code>한 값으로 평가된다는 걸 간과해서 테스트케이스 하나를 통과시키지 못했다.

  - 숫자형 값 중 0만 <code>falsy</code>한 값으로 평가, 나머지는 <code>truthy</code>한 값으로 평가
