
#started to check only neihbours, did not read the task completely
#Check if all trees on same row/column are lower than current tree
#the code works as of now, but could definitely be written better and more efficiently

class Tree():
    def __init__(self,height,row,column):
        self.height=int(height)
        self.row=row 
        self.column=column
        self.left=[]
        self.right=[]
        self.upper=[]
        self.lower=[]
    def getColumn(self):
        return self.column
    def getRow(self):
        return self.row
    def visible_tree(self):
        neighbours=[self.left,self.right,self.upper,self.lower]
        if None in neighbours:
            return True
        #elif self.height>self.left.height and self.height>self.right.height and self.height>self.upper.height and self.height>self.lower.height:
        #    return True
        blocked_left=False
        blocked_right=False
        blocked_upper=False
        blocked_lower=False
        for neighbour in self.left:
            if neighbour.height>=self.height:
                blocked_left=True
        for neighbour in self.right:
            if neighbour.height>=self.height:
                blocked_right=True
        for neighbour in self.upper:
            if neighbour.height>=self.height:
                blocked_upper=True
        for neighbour in self.lower:
            if neighbour.height>=self.height:
                blocked_lower=True
        if False in [blocked_left,blocked_right,blocked_upper,blocked_lower]:
            return True 
        else:
            return False
    def scenic_view(self):
        neighbours=[self.left,self.right,self.upper,self.lower]
        #print(neighbours)
        #print("***")
        if None in neighbours:
            return 0
        view_left=0
        view_right=0
        view_upper=0
        view_lower=0
        print("This tree")
        print(self)
        for neighbour in self.left:
            print("left nabo")
            print(neighbour)
            if neighbour.height<self.height:
                view_left+=1
            elif neighbour.height>=self.height:
                view_left+=1
                break
        for neighbour in self.right:
            print("right nabo")
            print(neighbour)
            if neighbour.height<self.height:
                view_right+=1
            elif neighbour.height>=self.height:
                view_right+=1
                break
        for neighbour in self.upper:
            print("upper nabo")
            print(neighbour)
            if neighbour.height<self.height:
                view_upper+=1
            elif neighbour.height>=self.height:
                view_upper+=1
                break
        for neighbour in self.lower:
            print("lower nabo")
            print(neighbour)
            if neighbour.height<self.height:
                view_lower+=1
            elif neighbour.height>=self.height:
                view_lower+=1
                break
        print(view_left,view_right,view_upper,view_lower)
        print(view_left*view_right*view_upper*view_lower)
        return view_left*view_right*view_upper*view_lower
    def __str__(self):
        str=f'Height: {self.height}'
        return str

def populateNeighbours(list,max_rows,max_columns):
    for tree in list:
        this_column=tree.getColumn()
        this_row=tree.getRow()
        left_column=range(this_column)
        left_row=this_row
        right_column=range(this_column+1,max_columns)
        right_row=this_row
        upper_column=this_column
        upper_row=range(this_row)
        lower_column=this_column
        lower_row=range(this_row+1,max_rows)
        for compareTree in list:
            compareTree_column=compareTree.getColumn()
            compareTree_row=compareTree.getRow()
            if compareTree_column in left_column and compareTree_row == left_row:
                tree.left.append(compareTree)
            elif compareTree_column in right_column and compareTree_row == right_row:
                tree.right.append(compareTree)
            elif compareTree_column == upper_column and compareTree_row in upper_row:
                tree.upper.append(compareTree)
            elif compareTree_column == lower_column and compareTree_row in lower_row:
                tree.lower.append(compareTree)

def populateNeighboursScenic(list,max_rows,max_columns):
    for tree in list:
        this_column=tree.getColumn()
        this_row=tree.getRow()
        left_column=range(this_column)
        left_row=this_row
        right_column=range(this_column+1,max_columns)
        right_row=this_row
        upper_column=this_column
        upper_row=range(this_row)
        lower_column=this_column
        lower_row=range(this_row+1,max_rows)
        for compareTree in list:
            compareTree_column=compareTree.getColumn()
            compareTree_row=compareTree.getRow()
            if compareTree_column in left_column and compareTree_row == left_row:
                tree.left.append(compareTree)
            elif compareTree_column in right_column and compareTree_row == right_row:
                tree.right.append(compareTree)
            elif compareTree_column == upper_column and compareTree_row in upper_row:
                tree.upper.append(compareTree)
            elif compareTree_column == lower_column and compareTree_row in lower_row:
                tree.lower.append(compareTree)
    #sort neighbours in correct order so that they go 'outwards' from the 'mother tree'
    for tree in list:
        tree.left.sort(key=lambda x:x.column,reverse=True)
        tree.right.sort(key=lambda x:x.column,reverse=False)
        tree.upper.sort(key=lambda x:x.row,reverse=True)
        tree.lower.sort(key=lambda x:x.row,reverse=False)

def main():
    with open('8_input.txt') as f:
        lines=f.read().splitlines()
        trees=[]
        rows = len(lines)
        columns = len(lines[0])
        for i in range(rows):
            for j in range(columns):
                trees.append(Tree(lines[i][j],i,j))
        populateNeighboursScenic(trees,rows,columns)
        visible=0
        scenic_view=[]
        for tree in trees:
            if tree.visible_tree():
                visible+=1
            scenic_view.append(tree.scenic_view())
        print(visible)
        print(max(scenic_view))


main()

#part 1: 1688
#part 2: 410400