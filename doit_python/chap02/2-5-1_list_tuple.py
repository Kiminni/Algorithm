list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

print(list1)
print(list2)

print(list1 is list2) # False -> literal(고정된 값)이 아님

list2 = list1 # list1을 참조
print(list1 is list2) # True

list1[2] = 9
print(list1)
print(list2)

