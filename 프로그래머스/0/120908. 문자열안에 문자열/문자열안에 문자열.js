function solution(str1, str2) {
    let answer = str1.search(str2);
    if(answer === -1) return 2;
    return 1;
}