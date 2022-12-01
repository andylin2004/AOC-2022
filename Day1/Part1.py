f = open("input.txt", 'r')
input = f.read().splitlines()

maxCal = 0
curTotal = 0
for line in input:
    line = line.strip()
    print(line)
    if line == '':
        maxCal = max(maxCal, curTotal)
        curTotal = 0
    else:
        curTotal += int(line)

print(maxCal)