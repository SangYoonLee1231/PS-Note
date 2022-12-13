// const fs = require("fs");
// const input = fs.readFileSync("./input.txt", "utf8").toString();
// // const input = fs.readFileSync("/dev/stdin", "utf8").toString();

// const inputTestCase = input.split("\n");
// const n = Number(inputTestCase[0]);
// const room = [];

// for (let i = 1; i <= n; i++) {
//   room.push(inputTestCase[i].split(""));
// }

// function solution(n, room) {
//   let [availableSeatRow, availableSeatCol] = [0, 0];

//   availableSeatRow = countAvailableSeat(n, room, "row");
//   availableSeatCol = countAvailableSeat(n, room, "col");

//   console.log(`${availableSeatRow} ${availableSeatCol}`);
// }

// function countAvailableSeat(n, room, dir) {
//   let availableSeatCount = 0;

//   for (let i = 0; i < n; i++) {
//     let straight = 0;

//     for (let j = 0; j < n; j++) {
//       let [a, b] = dir === "row" ? [i, j] : [j, i];
//       if (room[a][b] === ".") {
//         straight += 1;
//       } else {
//         straight = 0;
//       }
//       if (straight >= 2) {
//         availableSeatCount += 1;
//         break;
//       }
//     }
//   }

//   return availableSeatCount;
// }

// solution(n, room);

const fs = require("fs");
// let input = fs.readFileSync("./input.txt", "utf8").toString().trim();
let input = fs.readFileSync("/dev/stdin", "utf8").toString().trim();

input = input.split("\n");
let inputTestCase = input.map((item) => item.split(" "));
// int로 전환
inputTestCase = inputTestCase.map((item) => item.map((item) => Number(item)));

function solution(inputTestCase) {
  const x = inputTestCase[0][0];
  const n = inputTestCase[1][0];
  let totalPrice = 0;

  for (let i = 2; i < n + 2; i++) {
    let [price, amount] = inputTestCase[i];
    totalPrice += price * amount;
  }

  console.log(totalPrice === x ? "Yes" : "No");
}

solution(inputTestCase);
