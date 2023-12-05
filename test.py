import random
numberOfStreaks = 0

counter_heads = 0
counter_tails = 0

heads_tails= ["H", 'T']

for experimentNumber in range(1000):
    ranint = random.randint(0,1)
    if ranint == 0:
        counter_heads += 1
        counter_tails = 0
    else:
        counter_tails +=1
        counter_heads = 0
    
    if counter_heads or counter_tails == 6:
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
    
    # Code that creates a list of 100 'heads' or 'tails' values.

    # Code that checks if there is a streak of 6 heads or tails in a row.
