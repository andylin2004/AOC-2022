f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

max_sceneic = 0
for line in range(len(input)):
    for char in range(len(input[line])):
        scene_score = 1
        counter = 0
        for eval_line in range(line - 1, -1, -1):
            if int(input[eval_line][char]) >= int(input[line][char]):
                counter += 1
                break
            else:
                counter += 1
        scene_score *= counter
        counter = 0
        for eval_line in range(line + 1, len(input)):
            if int(input[eval_line][char]) >= int(input[line][char]):
                counter += 1
                break
            else:
                counter += 1
        scene_score *= counter
        counter = 0
        for eval_char in range(char - 1, -1, -1):
            if int(input[line][eval_char]) >= int(input[line][char]):
                counter += 1
                break
            else:
                counter += 1
        scene_score *= counter
        counter = 0
        for eval_char in range(char + 1, len(input[line])):
            if int(input[line][eval_char]) >= int(input[line][char]):
                counter += 1
                break
            else:
                counter += 1
        scene_score *= counter
        max_sceneic = max(max_sceneic, scene_score)
                
print(max_sceneic)