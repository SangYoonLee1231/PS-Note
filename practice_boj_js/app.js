function solution(s) {
  let answer = 0;
  let [sameWithX, diffWithX] = [0, 0];
  let x = "";
  let flag = false;

  for (let i in s) {
    if (flag) {
      if (s[i] === x) {
        sameWithX++;
      } else {
        diffWithX++;
      }

      if (sameWithX === diffWithX) {
        answer++;
        [sameWithX, diffWithX] = [0, 0];
        flag = false;
      }
    } else {
      x = s[i];
      sameWithX++;
      flag = true;
    }
  }

  if (!(sameWithX === 0 && diffWithX === 0)) {
    answer++;
  }

  return answer;
}

s = "abracadabra";
console.log(solution(s));
