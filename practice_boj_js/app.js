// 입력받기
const fs = require("fs");
let input = fs.readFileSync("/dev/stdin", "utf8");
// let input = fs.readFileSync("./input.txt").toString();
input = input.split("\n");
const [n, m] = input[0].split(" ");

// 입력값 정제
let newMatrixA = [];
let newMatrixB = [];

for (let i = 1; i < input.length; i++) {
  let newArr = input[i].split(" ");

  newArr = newArr.map((item) => Number(item));

  if (i <= n) {
    newMatrixA.push(newArr);
  } else {
    newMatrixB.push(newArr);
  }
}

// 풀이
function solution(n, m, newMatrixA, newMatrixB) {
  const answerMatrix = [];

  for (let i = 0; i < n; i++) {
    answerMatrix.push([]);
    for (let j = 0; j < m; j++) {
      answerMatrix[i].push(newMatrixA[i][j] + newMatrixB[i][j]);
    }
  }

  return answerMatrix;
}

// 출력
let answerStr = "";
let answerMatrix = solution(n, m, newMatrixA, newMatrixB);

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    answerStr += `${answerMatrix[i][j]} `;
  }
  answerStr += `\n`;
}

console.log(answerStr);
