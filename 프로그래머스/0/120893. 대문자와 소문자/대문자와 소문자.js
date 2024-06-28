function solution(my_string) {
    result = ""
    for (const e of my_string) {
        if ('a' <= e && e <= 'z') result += e.toUpperCase();
        else if ('A' <= e && e <= 'Z') result += e.toLowerCase();
    }
    return result;
}