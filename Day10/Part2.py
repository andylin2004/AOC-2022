f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

position = 1
line = 0
cycle = 1
start_exec_cycle = None

screen = [[" " for h in range(40)] for x in range(6)]

while line < len(input):
    if position % 40 == cycle % 40 or position % 40 + 1 == cycle % 40 or position % 40 + 2 == cycle % 40:
        print(cycle - 1)
        screen[(cycle - 1) // 40][(cycle - 1) % 40] = "#"
    if start_exec_cycle is not None and cycle - start_exec_cycle  == 1:
        position += int(input[line][5:])
        start_exec_cycle = None
        line += 1
    elif start_exec_cycle is None:
        if input[line][:4] == "addx":
            start_exec_cycle = cycle
        elif input[line][:4] == "noop":
            line += 1

    cycle += 1

for line in screen:
    for char in line:
        print(char, end="")
    print()
