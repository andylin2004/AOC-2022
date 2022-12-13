import ast
f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

def compare_recursive(left_arr: list, right_arr: list):
    for i in range(max(len(left_arr), len(right_arr))):
        if i >= len(left_arr):
            return True
        elif i >= len(right_arr):
            return False
        # print(left_arr[i], right_arr[i])
        if type(left_arr[i]) is not type(right_arr[i]):
            if type(left_arr[i]) is int:
                result = compare_recursive([left_arr[i]], right_arr[i])
            else:
                result = compare_recursive(left_arr[i], [right_arr[i]])
            if result is not None:
                return result
        elif type(left_arr[i]) is list and type(right_arr[i]) is list:
            result = compare_recursive(left_arr[i], right_arr[i])
            if result is not None:
                return result
        else:
            if left_arr[i] > right_arr[i]:
                return False
            elif left_arr[i] < right_arr[i]:
                return True

left = None
right = None
indice = 1
total = 0
for line in input:
    if line == "":
        left = None
        right = None
    else:
        if left is None:
            left = ast.literal_eval(line)
        else:
            right = ast.literal_eval(line)
            if compare_recursive(left, right):
                total += indice
            print(indice)
            indice += 1

print(total)