file_name = '8_input.txt'

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
        if self.nodeId == "AAA":
            return True
        return False
    
    def isEndNode(self):
        if self.nodeId == "ZZZ":
            return True
        return False
    
instruction=[]
nodes = {}
steps = 0
foundEnd = False

with open(file_name, 'r') as f:
    lines = f.readlines()
    instruction = [char for char in lines[0].strip()] #creating list with all characters
    for i in range(2, len(lines)):
        thisNode = Node(lines[i])
        nodes[thisNode.get_nodeId()] = thisNode
    currentNode = nodes["AAA"]
    while foundEnd == False:
        for i in range(len(instruction)):
            if instruction[i] == 'L':
                currentNode = nodes[currentNode.get_left()]
            elif instruction[i] == 'R':
                currentNode = nodes[currentNode.get_right()]
            steps += 1
            if currentNode.isEndNode():
                foundEnd = True

print("STEPS: ", steps)