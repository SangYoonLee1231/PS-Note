const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const inputCaseCount = +input[0];
const inputCase = [];

for (let i = 1; i <= inputCaseCount; i++) {
  inputCase.push(input[i].split(""));
}

solution(inputCase);

function solution(inputCase) {
  const score = inputCase.forEach((item) => {
    let score = 0;
    let tempScore = 0;

    score = item.reduce((acc, cur, idx) => {
      if (idx === item.length - 1) {
        if (cur === "O") {
          acc += tempScore + 1;
        }
        return acc;
      }

      if (cur === "O") {
        tempScore += 1;
        acc += tempScore;
      }

      if (cur === "X") {
        tempScore = 0;
      }

      return acc;
    }, 0);

    console.log(score);
  });
}
