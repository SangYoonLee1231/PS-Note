function solution(num) {
    if (num >= 0) {
        return (num % 2) ? "Odd" : "Even";    
    } else {
        return ((-num) % 2) ? "Odd" : "Even";
    }
}