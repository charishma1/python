"""Lists: Flexible , Mutable"""
#making list
my_list = [1, 2, 3, 4, 5]
print("my_lis:", my_list)
generated = list(range (1, 6))
print("generated:" , generated)

#access list items
print("my_list[0]:", my_list[-1])
nested_list = [1, 2, 3, [4, 5, 6], [[7, 8, 9]]]
print("nested_list", nested_list[2])
print("nested_list", nested_list[4][0][1])

#changing value in list
my_list[4] = "chnaged"
print("my_lis:", my_list)