f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

val = 1
strength = 0
line = 0
cycle = 1
start_exec_cycle = None
strength_count = 0

while line < len(input):
    if cycle % 40 == 20:
        strength += cycle * val
        strength_count += 1
        if strength_count == 6:
            break
    if start_exec_cycle is not None and cycle - start_exec_cycle  == 1:
        val += int(input[line][5:])
        start_exec_cycle = None
        line += 1
    elif start_exec_cycle is None:
        if input[line][:4] == "addx":
            start_exec_cycle = cycle
        elif input[line][:4] == "noop":
            line += 1

    cycle += 1
    
print(strength)
