const fs = require("fs");
// const input = fs.readFileSync("./input.txt", "utf8");
const input = fs.readFileSync("dev/stdin", "utf8");

let inputTestCase = input.split(" ");
inputTestCase = inputTestCase.map((item) => parseInt(item));

function solution(inputTestCase) {
  const [first, second, third] = inputTestCase;
  let prize = 0;

  if (first === second && second === third) {
    prize = 10000 + first * 1000;
  } else if (first === second || first === third) {
    prize = 1000 + first * 100;
  } else if (second === third) {
    prize = 1000 + second * 100;
  } else {
    prize = Math.max(...inputTestCase) * 100;
  }

  console.log(prize);
}

solution(inputTestCase);
