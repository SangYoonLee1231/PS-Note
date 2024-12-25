// function solution(numbers) {
//   let answer = 45;
//   numbers.forEach((item) => {
//     answer -= item;
//   })

//   return answer;
// }

function solution(numbers) {
  let answer = 0;
    
  for (let i = 0; i <= 9; i++) {
    answer += (numbers.includes(i)) ? 0 : i
  }
      
  return answer;
}