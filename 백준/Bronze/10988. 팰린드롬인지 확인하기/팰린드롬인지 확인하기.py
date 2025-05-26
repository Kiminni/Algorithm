string = input()
list_string = list(string) # [l, e, v, e, l]
reverse_string = "".join(reversed(list_string))
            
if string == reverse_string:
    print(1)
else:
    print(0)
