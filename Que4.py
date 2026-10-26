#There is a list with some numbers. Create a new dictionary using this list in such a way that key is number and value is frequency of occurrence of that number in list.
#[1,3,4,1,2,3,6,7,1,2,4]

numb = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]
freq_dict = {}

for num in numb:
    if num in freq_dict:
        freq_dict[num] += 1
    else:
        freq_dict[num] = 1

print(freq_dict)


