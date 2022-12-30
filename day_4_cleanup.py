def get_range_as_set(inp): #6-8 should return {6,7,8}
    numbers=inp.split("-") #split by hyphen
    return set(range(int(numbers[0]),int(numbers[1])+1)) #plus one to also include upper range limit

def get_range(inp): #6-8 should return range(6,9)
    numbers=inp.split("-") #split by hyphen
    return range(int(numbers[0]),int(numbers[1])+1) #plus one to also include upper range limit

#this returns true if any of the values overlap
def range_overlapping(x,y):
    if x.start == x.stop or y.start == y.stop:
         return False
    return x.start <= y.stop and y.start <= x.stop

def firstpart():
    with open('4_input.txt') as f:
        count=0
        for line in f:
            line=line.strip().split(",") # remove \n
            first=get_range_as_set(line[0])
            second=get_range_as_set(line[1])
            if first.issubset(second) or second.issubset(first): #check if any is subset of the other
                count+=1
    return count
#790 is too high, just checked overlapping values
#575 is also too high, upper range limit was not included
#513 is correct

def secondpart():
    with open('4_input.txt') as f:
        count=0
        for line in f:
            line=line.strip().split(",") # remove \n
            first=get_range(line[0])
            second=get_range(line[1])
            print(first)
            print(second)
            if range_overlapping(first,second):
                count+=1
            print(count)
    return count
#946 is too high

def secondpart2():
    with open('4_input.txt') as f:
        count=0
        for line in f:
            line=line.strip().split(",") # remove \n
            first=get_range_as_set(line[0])
            second=get_range_as_set(line[1])
            common_items=first.intersection(second) #find intersecting values
            if(len(common_items)>0): #if the sets have any intersecting values, it should be counted
                count+=1
    return count
#878 is correct

print(firstpart())
print(secondpart())
print(secondpart2())