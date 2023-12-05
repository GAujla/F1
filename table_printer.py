tableData = [['apples', 'oranges', 'cherries', 'banana'],
         ['Alice', 'Bob', 'Carol', 'David'],
         ['dogs', 'cats', 'moose', 'goosee']]


colWidths = [0] * len(tableData)




for line in range(len(tableData)):
    for word in range(len(tableData[line])):
        if colWidths[line] <= len(tableData[line][word]):
            colWidths[line] = len(tableData[line][word])
        else:
            colWidths[line] = colWidths[line]

#this is the part where you struggled
for li in range(len(tableData[0])):
    for i in range(len(tableData)):
        print(tableData[i][li].rjust(colWidths[i]), end =" ")
    print()