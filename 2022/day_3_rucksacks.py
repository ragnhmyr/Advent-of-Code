def firstpart():
    priorities=[]
    with open('3_input.txt') as f:
        i=1
        for line in f:
            line=line.strip() # remove \n
            print(f'rucksack {i}')
            i+=1        
            #always an even number of items since 'A given rucksack always has the same number of items in each of its two compartments'
            firstcompartment, secondcompartment = line[:len(line)//2], line[len(line)//2:]
            print(firstcompartment, secondcompartment)
            common_item="".join(set(firstcompartment).intersection(secondcompartment))
            print(common_item)
            #Lowercase item types a through z have priorities 1 through 26.
            #Uppercase item types A through Z have priorities 27 through 52.
            #ord(letter) gives the ascii code
            priority=0
            if common_item.isupper():
                priority=ord(common_item)-38
            elif common_item.islower():
                priority=ord(common_item)-96
            priorities.append(priority)
    return sum(priorities)

def secondpart():
    priorities=[]
    with open('3_input.txt') as f:
        all = f.read().splitlines()
        i=0
        while i<=len(all)-3:
            first=set(all[i])
            second=set(all[i+1])
            third=set(all[i+2])
            common_item="".join(first & second & third) # to get common item as string not set 
            priority=0 
            #print(f'first: {first}, second {second}, third {third}')
            #print(common_item)
            if common_item.isupper():
                 priority=ord(common_item)-38
            elif common_item.islower():
                 priority=ord(common_item)-96
            priorities.append(priority)
            i+=3
    return sum(priorities)

firstpart = print(firstpart())
secondpart = print(secondpart())
