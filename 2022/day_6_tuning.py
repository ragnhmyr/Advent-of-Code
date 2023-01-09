with open('6_input.txt') as f:
    string=f.read()
    print(string)
    i=0
    while i<len(string)-14:
        substring=string[i:i+14]
        substringset=set(substring) #create a set of the four characters, so that duplicated values are omitted
        if len(substringset)==14:
            print(i+14)
            print(substringset)
            break
        i+=1
        #1236 is too high, because increased i before end of while loop
        #1232 is too low
        #1235 is correct

        #for part 2: 3051 is correct
