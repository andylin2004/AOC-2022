f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

rucksack_a = []
common = None
total = 0
for line in input:
    rucksack_a = []
    common = None
    add_chars = len(line) // 2
    i = 0
    for char in line:
        if i < add_chars:
            rucksack_a.append(char)
            i += 1
        else:
            if char in rucksack_a:
                common = char
    # print(common)
    if ord(common) >= 97:
        total += ord(common) - 96
    else:
        total += ord(common) - 38

print(total)
