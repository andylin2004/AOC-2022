f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

points = 0
for line in input:
    parts = line.split()
    if parts[1] == 'X': # lose
        if parts[0] == 'A': # rock
            points += 3
        elif parts[0] == 'B': # paper
            points += 1
        elif parts[0] == 'C': # scissor
            points += 2
    elif parts[1] == 'Y': # draw
        points += 3
        if parts[0] == 'A': # rock
            points += 1
        elif parts[0] == 'B': # paper
            points += 2
        elif parts[0] == 'C': # scissor
            points += 3
    elif parts[1] == 'Z': #win
        points += 6
        if parts[0] == 'A': # rock
            points += 2
        elif parts[0] == 'B': # paper
            points += 3
        elif parts[0] == 'C': # scissor
            points += 1

print(points)