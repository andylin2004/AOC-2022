import ast
f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

class DataPack:
    def __init__(self, line) -> None:
        self.data = ast.literal_eval(line)

    def __lt__(self, other):
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
        
        return compare_recursive(self.data, other.data)


    def __repr__(self) -> str:
        return str(self.data)

array = [DataPack("[[2]]"), DataPack("[[6]]")]
for line in input:
    if line != "":
        array.append(DataPack(line))

array.sort()
result = 1
for i in range(len(array)):
    print(array[i])
    if array[i].data == [[2]] or array[i].data == [[6]]:
        result *= (i + 1)

print(result)