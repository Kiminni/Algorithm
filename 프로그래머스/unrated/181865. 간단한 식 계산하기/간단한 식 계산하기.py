def solution(binomial):
    tmp = binomial.split(" ")
    if tmp[1] == "+":
        return int(tmp[0]) + int(tmp[2])
    if tmp[1] == "-":
        return int(tmp[0]) - int(tmp[2])
    if tmp[1] == "*":
        return int(tmp[0]) * int(tmp[2])