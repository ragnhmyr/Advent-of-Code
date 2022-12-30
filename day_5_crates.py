import numpy as np

def command(line): #get list of move,from,to
    list=line.split()
    a=int(list[1]) #move
    b=int(list[3]) #from
    c=int(list[5]) #to
    return [a,b,c]

def move_crates_9000(crate_list,command):
    crates_to_move=command[0]
    from_crate=command[1]-1
    to_crate=command[2]-1
    for i in range(crates_to_move):
        crate=crate_list[from_crate].pop(0) #removes the first item of the list
        crate_list[to_crate].insert(0,crate) #inserts the removed item to the correct list

def move_crates_9001(crate_list,command):
    crates_to_move=command[0]
    from_crate=command[1]-1
    to_crate=command[2]-1
    for i in range(crates_to_move-1,-1,-1):
        crate=crate_list[from_crate].pop(i) #removes the first item of the list
        crate_list[to_crate].insert(0,crate) #inserts the removed item to the correct list
    #print(crate_list)
    #print("***\n")
    #QRQFHFWCL was correct


with open('5_input.txt') as f:
    crates=[[] for i in range(8)]
    count=0
    commands=[]
    for line in f:
        line=line.strip("\n")
        if '[' in line:
            i=0
            while i<=len(line):
                crates[count].append(line[i:i+3])
                i+=4
            count+=1
        elif 'move' in line:
            commands.append(command(line))
    for i in range(len(crates)):
        crates[i]=[x.strip() for x in crates[i]] #get rid of leading and trailing zeros
    crate_transpose=np.array(crates).T.tolist()
    for i in range(len(crate_transpose)):
        while ("" in crate_transpose[i]):
            crate_transpose[i].remove("")
    #print(crate_transpose)
    #print(commands)
    '''
    first part
    for i in range(len(commands)):
        move_crates_9000(crate_transpose,commands[i])
    print(crate_transpose)
    '''
    #second part
    for i in range(len(commands)):
        move_crates_9001(crate_transpose,commands[i])
    #print(crate_transpose)
    #to get the string as output
    str=""
    for i in range(len(crate_transpose)):
        letter=crate_transpose[i][0].replace("[","")
        str+=letter.replace("]","")
    print(str)

#TLFGBZHCN is correct




