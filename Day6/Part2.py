f = open("input.txt", 'r')
f = open("test_input.txt", 'r')
input = f.read()

run = True
for i in range(len(input)):
    for v in range(4):
        if input[i:i+4].count(input[i+v]) > 1:
            break
        if v == 3:
            print(i+4)
            run = False
    if not run:
        break