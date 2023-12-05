spam = ['apples', 'bannas', 'tofu', 'cats', 1]


print(spam[0:-1])

new_string = "'"
index = spam[:-2]

for i in spam[:-1]:
    new_string = new_string + str(i) + ', '

new_string = new_string + 'and ' + str(spam[-1]) + "'"
print(new_string)