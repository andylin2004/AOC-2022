f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

rucksack_a = []
common_ab = []
common_all = None
total = 0
line_count = 0
for line in input:
    if line_count % 3 == 0:
        rucksack_a = [x for x in line]
        print(rucksack_a)
    elif line_count % 3 == 1:
        for char in line:
            if char in rucksack_a:
                common_ab.append(char)
    else:
        for char in line:
            if char in common_ab:
                common_all = char
        if ord(common_all) >= 97:
            total += ord(common_all) - 96
        else:
            total += ord(common_all) - 38
        rucksack_a = []
        common_ab = []
        common_all = None
    line_count += 1

print(total)
