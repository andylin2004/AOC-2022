import re
from collections import deque

f = open("input.txt", 'r')
f = open("test_input.txt", 'r')
input = f.read().splitlines()

stacks = [deque() for _ in input[input.index("") - 1].split()]
move = False
pattern = re.compile("move ([0-9]+) from ([0-9]) to ([0-9])")

for line in input:
    if line == "":
        move = True
        print(stacks)
    elif move:
        m = pattern.match(line)
        qty = int(m.group(1))
        origin = int(m.group(2)) - 1
        end = int(m.group(3)) - 1
        for _ in range(qty):
            stacks[end].append(stacks[origin].pop())
    elif not move and not line.startswith("move"):
        split = []
        for i in range(0, len(line), 4):
            print(line[i+1])
            if line[i+1] != " " and line[i+1] != "" and not line[i+1].isdigit():
                stacks[i // 4].appendleft(line[i+1])
        
print("".join([x[-1] for x in stacks]))