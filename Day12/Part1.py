import heapq

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

dx = [0,1,0,-1]
dy = [1,0,-1,0]

array = []
results = []
start_x = 0
start_y = 0
end_x = 0
end_y = 0
for line in range(len(input)):
    line_arr = []
    for char in range(len(input[line])):
        line_arr.append(input[line][char])
        if input[line][char] == "E":
            end_x = line
            end_y = char
        elif input[line][char] == "S":
            start_x = line
            start_y = char
    array.append(line_arr)


def dij(array): #dijkastra algo for pathcounting

    # three arrays
    results = [[10000] * len(array[0]) for _ in range(len(array))] # for keeping the least number of steps to get to an array slot
    isVisited = [[False] * len(array[0]) for _ in range(len(array))] # one for keeping track of if we already determined the least number of steps to get to an array slot
    pq = [] # for keeping track of next min slot to go to
 
    pq.append([0, (start_x, start_y)]) # preprocessing start place so we can kickstart checking the neighbors later
    results[start_x][start_y] = 0 # preprocessing the start, as it doesn't count at all and we don't want anything bad to happen

    heapq.heapify(pq) # dijkstra uses a priority queue

    while len(pq) > 0:
        u = heapq.heappop(pq) # pop out the thing in the array where the tentative (first indice) value is the least of all of them, because we are very sure that is the min
        x = u[1][0]
        y = u[1][1]
        if isVisited[x][y]: # just in case it pops up again sometime later and we already did it with a better case scenario
            continue
        for cx,cy in zip(dx,dy):
            if 0 <= x+cx < len(array) and 0 <= y+cy < len(array[0]) and ((array[x+cx][y+cy] == "E" and array[x][y] == "z") or (array[x+cx][y+cy] != "E" and ord(array[x+cx][y+cy]) - ord(array[x][y]) <= 1) or array[x][y] == "S"):
                newDist = results[x][y] + 1 # newDist is the tentative distance plus the number at a neighbor specified
                if results[x+cx][y+cy] > newDist: # we want the least num of steps to the neighbor as possible, so keep the min of the two for the tentative result
                    results[x+cx][y+cy] = newDist
                    heapq.heappush(pq, [newDist, (x+cx, y+cy)]) # we will handle the neighbor's neighbors later, once we are more sure that this is the min it can go
        
        isVisited[x][y] = True

    for row in results:
        print(row)

    return results[end_x][end_y]

print(dij(array))