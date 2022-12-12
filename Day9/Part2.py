from collections import deque

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
# f = open("test_input_2.txt", 'r')
input = f.read().splitlines()

area = [[0 for _ in range(26)] for _ in range(21)]
rope = [[10, 10] for _ in range(10)]
total = 0

area = [[0 for _ in range(10000)] for _ in range(10000)]
rope = [[50, 50] for _ in range(10)]
total = 0

def renderArea():
    # def check_tail(row, col):
    #     for i in range(9):
    #         if rope[i][0] == row and rope[i][1] == col:
    #             return True
    #     return False

    # for table_row in range(len(area)):
    #     for table_col in range(len(area[table_row])):
    #         if table_col == rope[9][1] and table_row == rope[9][0]:
    #             print("H", end="")
    #         elif check_tail(table_row, table_col):
    #             print("T", end="")
    #         elif area[table_row][table_col] == 0:
    #             print(".", end="")
    #         else:
    #             print(area[table_row][table_col], end="")
    #     print()
    # print(rope)
    # print()
    pass

def move_tail():
    for i in range(8, -1, -1):
        if rope[i][0] - rope[i+1][0] >= 2 and rope[i+1][1] == rope[i][1]:
            rope[i][0] -= 1
        elif rope[i+1][0] - rope[i][0] >= 2 and rope[i+1][1] == rope[i][1]:
            rope[i][0] += 1
        elif rope[i][1] - rope[i+1][1] >= 2 and rope[i+1][0] == rope[i][0]:
            rope[i][1] -= 1
        elif rope[i+1][1] - rope[i][1] >= 2 and rope[i+1][0] == rope[i][0]:
            rope[i][1] += 1
        elif rope[i][0] - rope[i+1][0] >= 2 and rope[i][1] - rope[i+1][1] >= 1:
            rope[i][0] -= 1
            rope[i][1] -= 1
        elif rope[i+1][0] - rope[i][0] >= 2 and rope[i][1] - rope[i+1][1] >= 1:
            rope[i][0] += 1
            rope[i][1] -= 1
        elif rope[i][0] - rope[i+1][0] >= 2 and rope[i+1][1] - rope[i][1] >= 1:
            rope[i][0] -= 1
            rope[i][1] += 1
        elif rope[i+1][0] - rope[i][0] >= 2 and rope[i+1][1] - rope[i][1] >= 1:
            rope[i][0] += 1
            rope[i][1] += 1
        elif rope[i][1] - rope[i+1][1] >= 2 and rope[i][0] - rope[i+1][0] >= 1:
            rope[i][0] -= 1
            rope[i][1] -= 1
        elif rope[i+1][1] - rope[i][1] >= 2 and rope[i][0] - rope[i+1][0] >= 1:
            rope[i][0] -= 1
            rope[i][1] += 1
        elif rope[i][1] - rope[i+1][1] >= 2 and rope[i+1][0] - rope[i][0] >= 1:
            rope[i][0] += 1
            rope[i][1] -= 1
        elif rope[i+1][1] - rope[i][1] >= 2 and rope[i+1][0] - rope[i][0] >= 1:
            rope[i][0] += 1
            rope[i][1] += 1

for line in input:
    print(line)
    direction = line[0]
    count = int(line[2:])
    if direction == "R":
        for i in range(count):
            rope[9][1] += 1
            move_tail()
            area[rope[0][0]][rope[0][1]] = 1
            # renderArea()
    elif direction == "L":
        for i in range(count):
            rope[9][1] -= 1
            move_tail()
            area[rope[0][0]][rope[0][1]] = 1
            # renderArea()
    if direction == "U":
        for i in range(count):
            rope[9][0] -= 1
            move_tail()
            area[rope[0][0]][rope[0][1]] = 1
            # renderArea()
    elif direction == "D":
        for i in range(count):            
            rope[9][0] += 1
            move_tail()
            area[rope[0][0]][rope[0][1]] = 1
            # renderArea()
    renderArea()
    print()

for table_row in area:
    for value in table_row:
        if value == 1:
            total += 1

renderArea()

print(total)