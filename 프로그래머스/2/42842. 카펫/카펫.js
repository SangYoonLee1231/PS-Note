// function solution(brown, yellow) {
//     let [row, col] = [0, 0];
    
//     for (let col = 1; col < 5000; col++) {
//         for (let row = 1; row < 5000; row++) {
//             if ((row * 2) + (col * 2) - 4 == brown && (row - 2) * (col - 2) == yellow) {
//                 return [row, col]
//             }     
//         }  
//     }
// }

function solution(brown, yellow) {
    let [row, col] = [0, 0];
    
    for (let col = 0; col < (brown+yellow); col++) {
        const row = Math.floor((brown + yellow) / col);
        
        if ((row * 2) + (col * 2) - 4 == brown) {
            if ((row - 2) * (col - 2) == yellow) {
                return [row, col]
            }
        }
    }
}