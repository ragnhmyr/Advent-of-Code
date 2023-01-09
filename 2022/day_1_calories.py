tot_calories=[]
with open('1_input.txt') as f:
    sum=0
    for line in f:
        line=line.strip() # remove \n 
        if line: #if line is not empty
            sum+=int(line) 
        else:
            tot_calories.append(sum) #the line is empty (go to next elf) and we can add the sum to the list
            sum=0 #set the sum to zero again
#first task
max=max(tot_calories) #answer to first task
#second task
tot_calories.sort() #sort the list
three_top=tot_calories[-1]+tot_calories[-2]+tot_calories[-3]
print(three_top)
        
