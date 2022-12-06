# 자바스크립트 PS 입출력 팁

<br/>

## 백준 문제 입출력 코드

- 입력값 (예)

  ```
  5
  5 50 50 70 80 100
  7 100 95 90 80 70 60 50
  3 70 90 80
  3 70 90 81
  9 100 99 98 97 96 95 94 93 91
  ```

<br/>

- JS 입력 코드 (문제에 따라 변형 가능)

  ```js
  const fs = require("fs"); // fs 모듈 사용
  let input = fs.readFileSync("/dev/stdin", "utf8").toString(); // raw Buffer -> string
  input = input.split("\n"); //
  const inputTestCase = [];

  const inputCount = input[0];

  for (let i = 1; i <= inputCount; i++) {
    const arr = input[i].split(" ");
    let newArr = [];

    for (let j = 0; j < arr.length; j++) {
      newArr.push(Number(arr[j]));
    }

    inputTestCase.push(newArr);
  }

  // solution 함수의 매개변수는 문제에 따라 맞게 설정해줄 수 있다.
  function solution(inputTestCase) {
    // 문제 풀이 코드 작성
  }

  solution(inputTestCase);
  ```