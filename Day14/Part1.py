f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

EMPTY = 0
ROCK = 1
SAND = 2
map = [[0] * 1000 for _ in range(1000)]
total = 0


for line in input:
    pair_strs = line.split(" -> ")
    pairs = []
    for pair_str in pair_strs:
        pair = pair_str.split(',')
        pairs.append((int(pair[0]), int(pair[1])))
    # print(pairs)
    for i in range(len(pairs) - 1):
        if pairs[i + 1][0] - pairs[i][0] != 0:
            for v in range(min(pairs[i][0], pairs[i+1][0]), max(pairs[i][0], pairs[i+1][0]) + 1):
                map[pairs[i][1]][v] = ROCK
                # print(v)
        elif pairs[i + 1][1] - pairs[i][1] != 0:
            for v in range(min(pairs[i][1], pairs[i+1][1]), max(pairs[i][1], pairs[i+1][1]) + 1):
                map[v][pairs[i][0]] = ROCK

for row in map[:100]:
    print(row[480:590])

while True:
    new_sand_x = 500
    new_sand_y = 0
    while new_sand_y + 1 < 1000 and 0 <= new_sand_x < 1000 and (map[new_sand_y + 1][new_sand_x] == 0 or map[new_sand_y + 1][new_sand_x - 1] == 0 or map[new_sand_y + 1][new_sand_x + 1] == 0):
        if map[new_sand_y + 1][new_sand_x] == 0:
            new_sand_y += 1
        elif map[new_sand_y + 1][new_sand_x - 1] == 0:
            new_sand_y += 1
            new_sand_x -= 1
        elif map[new_sand_y + 1][new_sand_x + 1] == 0:
            new_sand_y += 1
            new_sand_x += 1
    if new_sand_y + 1 >= 1000 or (new_sand_x < 0 or new_sand_x >= 1000):
        break
    else:
        total += 1
        print(total)
        map[new_sand_y][new_sand_x] = SAND

# for row in map:
#     print(row)
print(total)