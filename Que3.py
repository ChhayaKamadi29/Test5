#A list contains sublist with Emp information as follows : Data = [[101,”Seema”,45000],[340,”Rajani”,13000], [210,”Tannu”,14000],[320,”Suresh”,35000]]
#Write a program to sort the list based on salary.

data = [ [101, "Seema", 45000], [340, "Rajani", 13000], [210, "Tannu", 14000], [320, "Suresh", 35000]]

n = len(data)
for i in range(n):
    for j in range(0, n - i - 1):
        if data[j][2] > data[j + 1][2]:
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp

print(data)