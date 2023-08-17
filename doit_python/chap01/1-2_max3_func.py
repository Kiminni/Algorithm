def max3(a,b,c):
    maximum = a
    if maximum < b:
        maximum = b
    if maximum < c:
        maximum = c
    return maximum

print(f'max3(3,2,1) = {max3(3,2,1)}')