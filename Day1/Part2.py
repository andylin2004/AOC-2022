cals = []
total = 0

f = open("input.txt", 'r')
input = f.read().splitlines()

curTotal = 0
for line in input:
    line = line.strip()
    if line == '':
        cals.append(curTotal)
        curTotal = 0
    else:
        curTotal += int(line)
cals.sort()
for i in range(len(cals) - 1, len(cals) - 4, -1):
    print(cals[i])
    total += cals[i]

print(total)