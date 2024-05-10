function solution(n) {
    const answer = [...n.toString()].reduce((acc, cur) => {
        acc += Number(cur);
        return acc
    }, 0)
    
    return answer;
}