function solution(nums) {
    const map = new Map();
    
    nums.forEach((elem) => {
        map.set(elem, (map.get(elem) || 0) + 1);
    })
    
    if (parseInt(nums.length / 2) <= map.size) {
        return parseInt(nums.length / 2);
    } else {
        return map.size;
    }
}