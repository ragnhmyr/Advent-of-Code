def rock_paper_scissor(letter):
    if letter =="A" or letter =="X":
        return 1 #rock
    elif letter=="B" or letter=="Y":
        return 2 #paper
    elif letter=="C" or letter=="Z":
        return 3 #scissor

def shape(score): #just to more easily check in print who the winner is
    if score == 1:
        return "rock"
    elif score == 2:
        return "paper"
    elif score == 3:
        return "scissor"

def game_score(score_opponent,score_you):
    game_score=0
    if score_opponent==score_you:
        game_score=3
    elif (score_opponent==1 and score_you==3):
        game_score=0
    elif (score_opponent==3 and score_you==1):
        game_score=6
    elif (score_opponent>score_you):
        game_score=0
    else:
        game_score=6
    return game_score

def tot_score(opponent,you):
    game=game_score(opponent,you)
    tot = game+you
    print(f'opponent: {opponent} {shape(opponent)}, you: {you} {shape(you)}, game score = {game}, tot score = {tot}')
    return tot

def round(letter):
    game_score=0 #also if the letter is X
    if letter=="Y":
        game_score=3 #draw
    elif letter=="Z":
        game_score=6 #you need to win
    return game_score

#part two: what score you need to get to get the wanted round output
def your_score(score_opponent,end): #get how many points (which shape) you have to choose
    you_score=0
    if end == 3:
        you_score=score_opponent #have to choose same as opponent
    elif end == 6: #you have to win
        if score_opponent==3:
            you_score=1
        else:
            you_score=score_opponent+1
    elif end == 0: #you have to loose
        if score_opponent == 1:
            you_score=3
        else:
            you_score=score_opponent-1
    return you_score


scores_1=[]
scores_2=[]

with open('2_input.txt') as f:
    i=1
    for line in f:
        line=line.strip() # remove \n
        print(f'game {i}')
        i+=1        
        scores_1.append(tot_score(rock_paper_scissor(line[0]),rock_paper_scissor(line[2])))
        scores_2.append(tot_score(rock_paper_scissor(line[0]),your_score(rock_paper_scissor(line[0]),round(line[2]))))
#first part 
#11325 too low, didn't include if you have rock and opponent have scissors
#11475 correct
tot_score_1=print(sum(scores_1))
#second part
tot_score_2=print(sum(scores_2))
#16862
