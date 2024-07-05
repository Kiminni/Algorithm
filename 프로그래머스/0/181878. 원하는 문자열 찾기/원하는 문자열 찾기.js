function solution(myString, pat) {
    let string = myString.toLowerCase();
    if(string.includes(pat.toLowerCase())) return 1;
    return 0;
}