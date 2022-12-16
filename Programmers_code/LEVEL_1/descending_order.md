## <a href="https://school.programmers.co.kr/learn/courses/30/lessons/12944">정수 내림차순으로 배치하기</a>

### Solution (JavaScript)

- 풀이한 날짜 : 2022-12-16

<br/>

```js
function solution(n) {
  n = n.toString().split("");
  let arrayN = n.map((item) => Number(item));

  arrayN.sort((a, b) => b - a);
  n = arrayN.join("");

  return Number(n);
}
```

<br/>

#### Logic

- 접근 방법 : 각 자리의 숫자들을 정렬하기 위해 새 배열에 숫자들을 담아 sort 메소드를 쓰기로 했다. 이때 배열에 숫자를 쉽게 담을 수 있도록 '문자열' 자료형을 중간 다리의 역할로 활용했다.

- 숫자열 문자열로 바꾸로 split 함수로 쪼개 배열로 만든다.

- 배열의 요소는 문자형이므로 다시 숫자형으로 바꿔준다.

- sort 함수를 통해 배열을 내림차순으로 정렬한다.

- 다시 배열을 문자열로 합치고 숫자로 형변환 해준다.

- 자료형 변환 과정 : 숫자 -> 문자 -> 배열 -> (배열 내 원소) 숫자 -> (정렬) -> 문자 -> 숫자

<br/>

#### Feeling

- 바로 로직을 생각해서 실수없이 풀었다.

- 형변환에 많이 익숙해진 것 같다.
