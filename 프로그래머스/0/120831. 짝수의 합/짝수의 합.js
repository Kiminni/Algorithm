function solution(n) {
    let ans = 0
    for (i = 0; i <= n; i++) {
        if(i % 2 === 0) {
            ans += i     
        }
    }
    return ans
}