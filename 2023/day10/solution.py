import math


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return self
    def __next__(self):
        self.idx += 1
        try:
            return self.data[self.idx-1]
        except IndexError:
            self.idx = 0
            raise StopIteration

    def addNode(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def printLL(self):
        current_node = self.head
        output = [current_node.data]
        while(current_node):
            output.append(current_node.data)
            current_node = current_node.next
        return output

def get_new_pos(curr, prev):
    symbol = two_d_arr[curr[0]][curr[1]]
    north = (curr[0]-1, curr[1])
    south = (curr[0]+1, curr[1])
    east = (curr[0], curr[1]+1)
    west = (curr[0], curr[1]-1)
    connections = []
    if symbol == '|':
        connections.append(south)
        connections.append(north)
    if symbol == '-':
        connections.append(east)
        connections.append(west)
    if symbol == 'L':
        connections.append(north)
        connections.append(east)
    if symbol == 'J':
        connections.append(north)
        connections.append(west)
    if symbol == '7':
        connections.append(south)
        connections.append(west)
    if symbol == 'F':
        connections.append(south)
        connections.append(east)
    pos_return = [pos for pos in connections if pos != prev][0]
    return pos_return, curr

def count_inside_loop(arr, linkedlist):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'S':
                arr[i][j] = 'F'
    inside_loop = False
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (i,j) in linkedlist:
                if arr[i][j] == 'J' or arr[i][j] == 'L' or arr[i][j] == '|':
                    inside_loop = not inside_loop
            if not (i,j) in linkedlist and inside_loop:
                count += 1
    print('Part 2:', count)


with open('input.txt') as f:
    two_d_arr = []
    for line in f.read().split('\n'):
        two_d_arr.append(list(line))

    current_pos = (0, 0)
    for i in range(len(two_d_arr)):
        for j in range(len(two_d_arr[i])):
            if two_d_arr[i][j] == 'S':
                current_pos = (i, j)
                break

    ll = LinkedList()
    ll.addNode(current_pos)
    prev_pos = current_pos
    current_pos = (current_pos[0]+1,current_pos[1])
    ll.addNode(current_pos)

    step = 1
    while two_d_arr[current_pos[0]][current_pos[1]] != 'S':
        step += 1
        current_pos, prev_pos = get_new_pos(current_pos, prev_pos)
        ll.addNode(current_pos)
    print('Part 1:',math.floor(step/2))
    all_in_loop = ll.printLL()
    count_inside_loop(two_d_arr, all_in_loop)