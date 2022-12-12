import re

f = open("input.txt", 'r')
f = open("test_input.txt", 'r')
input = f.read().splitlines()
count_monkeys = 1 + input.count("")

class Monkey:
    def __init__(self) -> None:
        self.items = []
        self.operation = None
        self.divisible_by = None
        self.true_throw = None
        self.false_throw = None
        self.inspect_count = 0

    def __repr__(self) -> str:
        return "Monkey with items " + str(self.items) + " operations " + str(self.operation) + " divisble by " + str(self.divisible_by) + " " + str(self.true_throw) + " " + str(self.false_throw) + " risk " + str(self.inspect_count)

monkeys = []
cur_monkey = None

for line in input:
    if line.find("Monkey") == 0:
        if cur_monkey is not None:
            monkeys.append(cur_monkey)
        cur_monkey = Monkey()
    elif line.strip().find("Starting") == 0:
        for i in line[18:].split(", "):
            cur_monkey.items.append(int(i))
    elif line.strip().find("Operation") == 0:
        regex = re.compile("Operation: new = old ([*+]) ([0-9]+|old)")
        e = regex.match(line.strip())
        cur_monkey.operation = e.groups()
    elif line.strip().find("Test") == 0:
        regex = re.compile("Test: divisible by ([0-9]+)")
        e = regex.match(line.strip())
        cur_monkey.divisible_by = int(e.group(1))
    elif line.strip().find("If true") == 0:
        regex = re.compile("If true: throw to monkey ([0-9]+)")
        e = regex.match(line.strip())
        cur_monkey.true_throw = int(e.group(1))
    elif line.strip().find("If false") == 0:
        regex = re.compile("If false: throw to monkey ([0-9]+)")
        e = regex.match(line.strip())
        cur_monkey.false_throw = int(e.group(1))

monkeys.append(cur_monkey)

for _ in range(20):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            result = monkey.items.pop(0)
            if monkey.operation == ('*', 'old'):
                result **= 2
            elif monkey.operation[0] == '*':
                result *= int(monkey.operation[1])
            elif monkey.operation[0] == '+':
                result += int(monkey.operation[1])
            # result //= 3
            if result % monkey.divisible_by == 0:
                monkeys[monkey.true_throw].items.append(result)
            else:
                monkeys[monkey.false_throw].items.append(result)
            monkey.inspect_count += 1

print(monkeys)
sorted_result = sorted(monkeys, key=lambda x: x.inspect_count, reverse=True)
print(sorted_result)
print(sorted_result[0].inspect_count * sorted_result[1].inspect_count)