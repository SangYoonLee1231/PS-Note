function solution(num) {
    count = 0;
    
    while(num !== 1) {
        if (num % 2) {
            // 홀수
            num = num * 3 + 1
        } else {
            // 짝수
            num = parseInt(num / 2)
        }
        
        count += 1;
        
        if (count > 500) {
            return -1;
        }
    }
    
    return count;
}