s = "3people unFollowed me";

let arrayS = s.split(" ");

console.log(arrayS);

arrayS.forEach((item) => {
  console.log(item);
  if (item[0].match(new RegExp(/^[a-z]/))) {
    arrayS[0][0] = item[0].toUpperCase();
  }
});

// console.log(arrayS);
console.log(arrayS.join(" "));
