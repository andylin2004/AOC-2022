f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

total_visible = 0
for line in range(len(input)):
    for char in range(len(input[line])):
        if line == 0 or line == len(input) - 1:
            total_visible += 1
        elif char == 0 or char == len(input[line]) - 1:
            total_visible += 1
        else:
            searching = True
            for eval_line in range(line - 1, -1, -1):
                if int(input[eval_line][char]) >= int(input[line][char]):
                    break
                elif eval_line == 0:
                    total_visible += 1
                    searching = False
            if searching:
                for eval_line in range(line + 1, len(input)):
                    if int(input[eval_line][char]) >= int(input[line][char]):
                        break
                    elif eval_line == len(input) - 1:
                        total_visible += 1
                        searching = False
            if searching:
                for eval_char in range(char - 1, -1, -1):
                    if int(input[line][eval_char]) >= int(input[line][char]):
                        break
                    elif eval_char == 0:
                        total_visible += 1
                        searching = False
            if searching:
                for eval_char in range(char + 1, len(input[line])):
                    if int(input[line][eval_char]) >= int(input[line][char]):
                        break
                    elif eval_char == len(input[line]) - 1:
                        total_visible += 1
                        searching = False
                
print(total_visible)