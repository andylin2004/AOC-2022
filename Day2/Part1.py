f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

points = 0
for line in input:
    parts = line.split()
    if parts[1] == 'X': # rock
        points += 1
        if parts[0] == 'A': # rock
            points += 3
        elif parts[0] == 'C': #scissor
            points += 6
    elif parts[1] == 'Y': # paper
        points += 2
        if parts[0] == 'A': # rock
            points += 6
        elif parts[0] == 'B': #paper
            points += 3
    elif parts[1] == 'Z': #scissors
        points += 3
        if parts[0] == 'B': # paper
            points += 6
        elif parts[0] == 'C': #scissor
            points += 3

print(points)