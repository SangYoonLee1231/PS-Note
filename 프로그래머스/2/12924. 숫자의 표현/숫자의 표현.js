function solution(n) {
    let count = 0;
    
    for (let i = 1; (n / i) >= (i / 2); i++) {
        if (i % 2) { // 홀수
            if (n % i == 0) count++;
        } else { // 짝수
            if (n % i == (i / 2)) count ++;
        }
    }
    
    return count;
}