const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split(" ");

const inputArr = input.map((item) => +item);

solution(inputArr);

function solution(inputArr) {
  // console.log(inputArr);
  ascendingArr = [1, 2, 3, 4, 5, 6, 7, 8];
  descendingArr = [8, 7, 6, 5, 4, 3, 2, 1];

  if (inputArr.toString() === ascendingArr.toString()) {
    console.log("ascending");
  } else if (inputArr.toString() === descendingArr.toString()) {
    console.log("descending");
  } else {
    console.log("mixed");
  }
}
