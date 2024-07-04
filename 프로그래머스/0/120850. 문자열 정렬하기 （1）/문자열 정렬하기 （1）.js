function solution(my_string) {
    let string = my_string.split("");
    let arr = [];
    for(const s of my_string) {
        if('0' <= s && s <='9') arr.push(Number(s));
    }
    return arr.sort((a,b) => a - b);
}