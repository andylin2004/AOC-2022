f = open("input.txt", 'r')
f = open("test_input.txt", 'r')
input = f.read()

run = True
for i in range(len(input)):
    for v in range(14):
        if input[i:i+14].count(input[i+v]) > 1:
            break
        if v == 13:
            print(i+14)
            run = False
    if not run:
        break
