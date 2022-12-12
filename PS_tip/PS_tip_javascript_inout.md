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
  // let input = fs.readFileSync("./input.txt").toString(); // VS Code에 풀 땐 txt 파일로 입력값 받음
  input = input.split("\n");
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

<br/>

- JS 출력 코드

  ```js
  let answerStr = ''

  // 출력값 정제
  ...
    answerStr += `${num1} + ${num2} \n`;
  ...

  console.log(answerStr);
  ```

<br/>

- 입력 시 문제에 따라 앞 뒤 공백을 제거해주어야 하는 <code>trim</code> 메소드를 input값에 붙여주어야 하는 경우가 있다.

  ```js
  const fs = require("fs");

  let input = fs.readFileSync("/dev/stdin").toString().trim();
  ```
