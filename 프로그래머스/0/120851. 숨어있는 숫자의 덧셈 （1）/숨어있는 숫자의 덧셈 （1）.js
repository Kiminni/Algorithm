function solution(my_string) {
    let split = Array.from(my_string);
    let answer = 0;
    for (const e of split) {
        if ('0' <= e && e <= '9') {
            answer += parseInt(e)
        }
    }
    
    return answer;
}   