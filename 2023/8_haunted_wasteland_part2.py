import time

file_name = '8_input.txt'

start_time = time.time()
class Node:
    def __init__(self, string):
        self.nodeId, self.left, self.right = self.get_node_from_string(string)

    def get_node_from_string(self, string):
        nodeId = string[0:3]
        left = string[7:10]
        right = string[12:15]
        return nodeId, left, right
    
    def get_nodeId(self):
        return self.nodeId

    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right

    def __str__(self):
        return self.nodeId + " " + self.left + " " + self.right
    
    def isStartNode(self):
        if self.nodeId[-1] == "A":
            return True
        return False
    
    def isEndNode(self):
        if self.nodeId[-1] == "Z":
            return True
        return False
    
instruction=[]
nodes = {}
steps = 0
foundEnd = False
node_list = []

with open(file_name, 'r') as f:
    lines = f.readlines()
    instruction = [char for char in lines[0].strip()] #creating list with all characters
    for i in range(2, len(lines)):
        thisNode = Node(lines[i])
        nodes[thisNode.get_nodeId()] = thisNode
        if thisNode.isStartNode():
            node_list.append(thisNode)
            print(thisNode)
    iterations = 0
    while foundEnd == False:
        for i in range(len(instruction)):
            print("ITERATION: ", iterations)
            countEnds = 0
            countEnds = sum(node.isEndNode() for node in node_list)
            if countEnds == len(node_list):
                foundEnd = True
                break
            for j in range(len(node_list)):
                #print(node_list[j], countEnds)
                if instruction[i] == 'L':
                    node_list[j] = nodes[node_list[j].get_left()]
                elif instruction[i] == 'R':
                    node_list[j] = nodes[node_list[j].get_right()]
            steps += 1
            iterations += 1
            if foundEnd == True:
                break
            
print("--- %s seconds ---" % (time.time() - start_time))
print("STEPS: ", steps)