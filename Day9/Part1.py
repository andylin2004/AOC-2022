f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

area = [[0 for _ in range(6)] for _ in range(6)]
head_x = 5
head_y = 0
tail_x = 5
tail_y = 0
moving_x = None
is_pivot = False
total = 0

area = [[0 for _ in range(10000)] for _ in range(10000)]
head_x = 5000
head_y = 0
tail_x = 5000
tail_y = 0
moving_x = None
is_pivot = False
total = 0

def renderArea():
    # for table_row in range(len(area)):
    #     for table_col in range(len(area[table_row])):
    #         if table_col == head_y and table_row == head_x:
    #             print("H", end="")
    #         elif table_col == tail_y and table_row == tail_x:
    #             print("T", end="")
    #         else:
    #             print(area[table_row][table_col], end="")
    #     print()
    # print()
    pass

for line in input:
    print(line)
    direction = line[0]
    count = int(line[2:])
    if direction == "R":
        for i in range(count):
            head_y += 1
            if tail_x - head_x >= 2 and head_y == tail_y:
                tail_x -= 1
            elif head_x - tail_x >= 2 and head_y == tail_y:
                tail_x += 1
            elif tail_y - head_y >= 2 and head_x == tail_x:
                tail_y -= 1
            elif head_y - tail_y >= 2 and head_x == tail_x:
                tail_y += 1
            elif tail_x - head_x >= 2 and tail_y - head_y >= 1:
                tail_x -= 1
                tail_y -= 1
            elif head_x - tail_x >= 2 and tail_y - head_y >= 1:
                tail_x += 1
                tail_y -= 1
            elif tail_x - head_x >= 2 and head_y - tail_y >= 1:
                tail_x -= 1
                tail_y += 1
            elif head_x - tail_x >= 2 and head_y - tail_y >= 1:
                tail_x += 1
                tail_y += 1
            elif tail_y - head_y >= 2 and tail_x - head_x >= 1:
                tail_x -= 1
                tail_y -= 1
            elif head_y - tail_y >= 2 and tail_x - head_x >= 1:
                tail_x -= 1
                tail_y += 1
            elif tail_y - head_y >= 2 and head_x - tail_x >= 1:
                tail_x += 1
                tail_y -= 1
            elif head_y - tail_y >= 2 and head_x - tail_x >= 1:
                tail_x += 1
                tail_y += 1
            area[tail_x][tail_y] = 1
            renderArea()
    elif direction == "L":
        for i in range(count):
            head_y -= 1
            if tail_x - head_x >= 2 and head_y == tail_y:
                tail_x -= 1
            elif head_x - tail_x >= 2 and head_y == tail_y:
                tail_x += 1
            elif tail_y - head_y >= 2 and head_x == tail_x:
                tail_y -= 1
            elif head_y - tail_y >= 2 and head_x == tail_x:
                tail_y += 1
            elif tail_x - head_x >= 2 and tail_y - head_y >= 1:
                tail_x -= 1
                tail_y -= 1
            elif head_x - tail_x >= 2 and tail_y - head_y >= 1:
                tail_x += 1
                tail_y -= 1
            elif tail_x - head_x >= 2 and head_y - tail_y >= 1:
                tail_x -= 1
                tail_y += 1
            elif head_x - tail_x >= 2 and head_y - tail_y >= 1:
                tail_x += 1
                tail_y += 1
            elif tail_y - head_y >= 2 and tail_x - head_x >= 1:
                tail_x -= 1
                tail_y -= 1
            elif head_y - tail_y >= 2 and tail_x - head_x >= 1:
                tail_x -= 1
                tail_y += 1
            elif tail_y - head_y >= 2 and head_x - tail_x >= 1:
                tail_x += 1
                tail_y -= 1
            elif head_y - tail_y >= 2 and head_x - tail_x >= 1:
                tail_x += 1
                tail_y += 1
            area[tail_x][tail_y] = 1
            renderArea()
    if direction == "U":
        for i in range(count):
            head_x -= 1
            if tail_x - head_x >= 2 and head_y == tail_y:
                tail_x -= 1
            elif head_x - tail_x >= 2 and head_y == tail_y:
                tail_x += 1
            elif tail_y - head_y >= 2 and head_x == tail_x:
                tail_y -= 1
            elif head_y - tail_y >= 2 and head_x == tail_x:
                tail_y += 1
            elif tail_x - head_x >= 2 and tail_y - head_y >= 1:
                tail_x -= 1
                tail_y -= 1
            elif head_x - tail_x >= 2 and tail_y - head_y >= 1:
                tail_x += 1
                tail_y -= 1
            elif tail_x - head_x >= 2 and head_y - tail_y >= 1:
                tail_x -= 1
                tail_y += 1
            elif head_x - tail_x >= 2 and head_y - tail_y >= 1:
                tail_x += 1
                tail_y += 1
            elif tail_y - head_y >= 2 and tail_x - head_x >= 1:
                tail_x -= 1
                tail_y -= 1
            elif head_y - tail_y >= 2 and tail_x - head_x >= 1:
                tail_x -= 1
                tail_y += 1
            elif tail_y - head_y >= 2 and head_x - tail_x >= 1:
                tail_x += 1
                tail_y -= 1
            elif head_y - tail_y >= 2 and head_x - tail_x >= 1:
                tail_x += 1
                tail_y += 1
            area[tail_x][tail_y] = 1
            renderArea()
    elif direction == "D":
        for i in range(count):            
            head_x += 1
            if tail_x - head_x >= 2 and head_y == tail_y:
                tail_x -= 1
            elif head_x - tail_x >= 2 and head_y == tail_y:
                tail_x += 1
            elif tail_y - head_y >= 2 and head_x == tail_x:
                tail_y -= 1
            elif head_y - tail_y >= 2 and head_x == tail_x:
                tail_y += 1
            elif tail_x - head_x >= 2 and tail_y - head_y >= 1:
                tail_x -= 1
                tail_y -= 1
            elif head_x - tail_x >= 2 and tail_y - head_y >= 1:
                tail_x += 1
                tail_y -= 1
            elif tail_x - head_x >= 2 and head_y - tail_y >= 1:
                tail_x -= 1
                tail_y += 1
            elif head_x - tail_x >= 2 and head_y - tail_y >= 1:
                tail_x += 1
                tail_y += 1
            elif tail_y - head_y >= 2 and tail_x - head_x >= 1:
                tail_x -= 1
                tail_y -= 1
            elif head_y - tail_y >= 2 and tail_x - head_x >= 1:
                tail_x -= 1
                tail_y += 1
            elif tail_y - head_y >= 2 and head_x - tail_x >= 1:
                tail_x += 1
                tail_y -= 1
            elif head_y - tail_y >= 2 and head_x - tail_x >= 1:
                tail_x += 1
                tail_y += 1
            area[tail_x][tail_y] = 1
            renderArea()
    print()

for table_row in area:
    for value in table_row:
        if value == 1:
            total += 1

print(total)