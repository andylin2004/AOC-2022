import re

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

class Dir:
    def __init__(self, name) -> None:
        self.size = 0
        self.subdir = []
        self.parent = None
        self.name = name
    
    def __repr__(self) -> str:
        return str(self.size) + self.name

reading_dir_content = False
root = Dir("/")
cur_dir = root
for line in input:
    if line.find("$") == 0:
        if line.find("cd") > 0:
            if line[5:] == "..":
                cur_dir.parent.size += cur_dir.size
                cur_dir = cur_dir.parent
            elif line[5:] != "/":
                new_dir = Dir(line[5:])
                new_dir.parent = cur_dir
                cur_dir.subdir.append(new_dir)
                cur_dir = new_dir
        if line.find("ls"):
            pass
    else:
        if line.find("dir") == -1:
            pattern = re.compile("([0-9]+) (\S+)")
            seeked = pattern.match(line)
            cur_dir.size += int(seeked.group(1))

while cur_dir.name != "/":
    cur_dir.parent.size += cur_dir.size
    cur_dir = cur_dir.parent

def recursive_part(dir):
    total = 0
    for i in dir.subdir:
        result = recursive_part(i)
        total += result
    if dir.size <= 100000:
        total += dir.size
    return total

p1 = recursive_part(root)
print(p1)

def clear_recursive(dir):
    print(root.size)
    best_min = None
    print(dir.subdir, dir)
    for i in dir.subdir:
        result = clear_recursive(i)
        if result is not None:
            if best_min is None:
                best_min = result
            else:
                best_min = min(best_min, result)
    print(dir.size, "rvf iuqwefh ")
    if best_min is not None:
        return best_min
    elif dir.size >= 30000000 - (70000000 - root.size):
        return dir.size
    else:
        return None

print(clear_recursive(root))