# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def addNode(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#
#         current_node = self.head
#         while(current_node.next):
#             current_node = current_node.next
#
#         current_node.next = new_node
#
#     def printLL(self):
#         current_node = self.head
#         while(current_node):
#             print(current_node.data)
#             current_node = current_node.next

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

    # ll = LinkedList()
    # ll.addNode(current_pos)
    prev_pos = current_pos
    current_pos = (current_pos[0]+1,current_pos[1])

    step = 1
    while two_d_arr[current_pos[0]][current_pos[1]] != 'S':
        step += 1
        current_pos, prev_pos = get_new_pos(current_pos, prev_pos)
    print(step/2)