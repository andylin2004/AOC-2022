f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

pairs = 0
for line in input:
    print(line)
    line_parts = line.split(",")
    left_range = line_parts[0].split("-")
    right_range = line_parts[1].split("-")
    
    if (int(left_range[0]) <= int(right_range[0]) and int(right_range[1]) <= int(left_range[1])) or (int(right_range[0]) <= int(left_range[0]) and int(left_range[1]) <= int(right_range[1])) or (int(left_range[1]) >= int(right_range[0]) and int(left_range[1]) <= int(right_range[1])) or (int(right_range[1]) >= int(left_range[0]) and int(right_range[1]) <= int(left_range[1])):
        pairs += 1

print(pairs)