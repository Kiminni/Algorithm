function solution(s1, s2) {
    let answer = 0;
    for(const e1 of s1) {
        for(const e2 of s2) {
            if(e1 === e2) answer += 1;
        }
    }
    return answer;
}