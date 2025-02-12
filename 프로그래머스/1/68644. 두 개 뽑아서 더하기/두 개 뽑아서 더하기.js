function solution(numbers) {
    const answer = [];
    let uniqueAnswer = [];
    
    for (let i = 0; i < numbers.length - 1; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            answer.push(numbers[i] + numbers[j]);
            const answerSet = new Set(answer);
            uniqueAnswer = [...answerSet].sort((a, b) => a - b);
        }
    }
    
    return uniqueAnswer;
}