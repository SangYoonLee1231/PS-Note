// function solution(myString) {
//     return myString.toLowerCase();
// }

function solution(myString) {
    const answer = [];
    
    for (const elem of myString) {
        if (elem > 'a'.charCodeAt() && elem < 'z'.charCodeAt()) {
            answer.push(elem)
        }
        else {
            answer.push(elem.toLowerCase())  
        }
    }
    
    return answer.join('');
}