// function solution(myString) {
//     return myString.toUpperCase();
// }

function solution(myString) {
    const answer = [];
    
    for (const elem of myString) {
        if ((elem.charCodeAt() >= 'a'.charCodeAt()) && (elem.charCodeAt() <= 'z'.charCodeAt())) {
            answer.push(String.fromCharCode(elem.charCodeAt() - 32));
            // answer.push(elem.toUpperCase());
        } else {
            answer.push(elem);
            // console.log('대문자');
        }
    }
    
    return answer.join('');
}