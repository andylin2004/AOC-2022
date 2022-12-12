import re
from collections import deque
from functools import cache

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()
count_monkeys = 1 + input.count("")

class NumOps:
    def __init__(self, operation, number) -> None:
        self.operation = operation
        self.number = int(number)
        self.next = None
        self.end = None

    def is_divisible(self, divide_by):
        node = self
        mod_result = 0
        while node is not None:
            if node.operation == '+':
                mod_result = (mod_result + (node.number % divide_by)) % divide_by
            elif node.operation == '*':
                mod_result = (mod_result * (node.number % divide_by)) % divide_by
            else:
                mod_result = mod_result ** 2 % divide_by
            node = node.next
        
        return mod_result == 0

    def __repr__(self) -> str:
        node = self
        mod_result = 0
        while node is not None:
            if node.operation == '+':
                mod_result = (mod_result + (node.number))
            elif node.operation == '*':
                mod_result = (mod_result * (node.number))
            else:
                mod_result = mod_result ** 2
            node = node.next
        return str(mod_result)


class Monkey:
    def __init__(self) -> None:
        self.items = deque()
        self.operation = None
        self.divisible_by = None
        self.true_throw = None
        self.false_throw = None
        self.inspect_count = 0

    def __repr__(self) -> str:
        return "Monkey with items " + str(self.items) + " operations " + str(self.operation) + " divisble by " + str(self.divisible_by) + " " + str(self.true_throw) + " " + str(self.false_throw) + " risk " + str(self.inspect_count)

def divisible_by(lst, divide_num):
    remainder_total = 0
    for num in lst:
        remainder_total += num % divide_num
    return remainder_total % divide_num == 0

monkeys = []
cur_monkey = None

for line in input:
    if line.find("Monkey") == 0:
        if cur_monkey is not None:
            monkeys.append(cur_monkey)
        cur_monkey = Monkey()
    elif line.strip().find("Starting") == 0:
        for i in line[18:].split(", "):
            cur_monkey.items.append(NumOps('+', i))
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

for _ in range(10000):
    print(_)
    for monkey in monkeys:
        while len(monkey.items) > 0:
            result = monkey.items.popleft()
            if monkey.operation == ('*', 'old'):
                new_result = NumOps("**", 2)
            else:
                new_result = NumOps(monkey.operation[0], monkey.operation[1])
            if result.end is None:
                result.end = new_result
                result.next = new_result
            else:
                result.end.next = new_result
                result.end = result.end.next
            if result.is_divisible(monkey.divisible_by):
                monkeys[monkey.true_throw].items.append(result)
            else:
                monkeys[monkey.false_throw].items.append(result)

            monkey.inspect_count += 1

# print(monkeys)

sorted_result = sorted(monkeys, key=lambda x: x.inspect_count, reverse=True)
# print(sorted_result)
print(sorted_result[0].inspect_count * sorted_result[1].inspect_count)