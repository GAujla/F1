grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


counter = 0

sequence = ""
while True:
    if counter == len(grid[0]):
        break
    for i in range(len(grid)):
        sequence = sequence + grid[i][counter]
        if i == 8 and counter == 5:
            counter += 1
        elif i == 8:
            counter += 1
            sequence = sequence + '\n'


print(sequence)
