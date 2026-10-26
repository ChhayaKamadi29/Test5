#Python Program to Find the Union of two Lists without using set concept.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

union_list = []

for item in list1:
    if item not in union_list:
        union_list.append(item)

for item in list2:
    if item not in union_list:
        union_list.append(item)

print("List 1:", list1)
print("List 2:", list2)
print("Union of two lists:", union_list)