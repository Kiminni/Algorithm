function solution(array, n) {
    num = 0
    for (let i = 0; i < array.length; i++) {
        if (array[i] === n) {
            num += 1           
        }
 
    }
    return num
}