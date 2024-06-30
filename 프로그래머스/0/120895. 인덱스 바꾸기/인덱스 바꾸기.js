function solution(my_string, num1, num2) {
    let ans = my_string.split("");
    let tmp = "";
    tmp = ans[num1];
    ans[num1] = ans[num2];
    ans[num2] = tmp;
    
    return ans.join("");
    
}