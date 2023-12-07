file_name = '7_input.txt'

#PART 2 
#from lowest to highest
card_strength = ["J","2","3","4","5","6","7","8","9","T","Q","K","A"]
hand_type = ["high-card", "one-pair", "two-pairs", "three-of-a-kind", "full-house", "four-of-a-kind", "five-of-a-kind"]

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.type = self.get_hand_type()

    def get_hand_type(self):
        character_dict = {i: self.cards.count(i) for i in self.cards}
        count_j = character_dict.get("J",0)
        if count_j > 0 and count_j < 5: #have to account for a hand with all jokers
            del character_dict["J"]
            #increase the maximum count of one character by number of Jokers
            max_key = max(character_dict, key=character_dict.get)
            character_dict[max_key] += count_j
        if 5 in character_dict.values():
            return "five-of-a-kind"
        elif 4 in character_dict.values():
            return "four-of-a-kind"
        elif 3 in character_dict.values(): #check for full house or three of a kind
            if 2 in character_dict.values():
                return "full-house"
            return "three-of-a-kind"
        elif 2 in character_dict.values(): #check for two pairs or one pair
            if list(character_dict.values()).count(2) > 1:
                return "two-pairs"
            else:
                return "one-pair"
        else:
            return "high-card"   

    def get_bid_times_rank(self, rank):
        return self.bid * rank
    
    #comparing two hands
    #they cant be equal according to the problem
    def __gt__(self, other):
        if hand_type.index(self.type) > hand_type.index(other.type):
            return True
        elif hand_type.index(self.type) < hand_type.index(other.type):
            return False
        else: # then it's equal, check the different types 
            for i in range(len(self.cards)):
                if card_strength.index(self.cards[i]) > card_strength.index(other.cards[i]):
                    return True
                elif card_strength.index(self.cards[i]) < card_strength.index(other.cards[i]):
                    return False
        return False
    
    def __lt__(self, other):
        if self>other:
            return False
        return True
    
with open(file_name) as f:
    lines = f.readlines()
    max_rank = len(lines)

    cards_list = []
    for i in range(len(lines)):
        [hand,bid] = lines[i].split()
        bid = int(bid) #make it to a number
        this_hand = Hand(hand, bid)
        cards_list.append(this_hand)
    
    #sort the cards_list
    sorted_cards_list = [] 
    for card in cards_list:
        if len(sorted_cards_list) == 0:
            sorted_cards_list.append(card)
        else:
            for i in range(len(sorted_cards_list)):
                if card < sorted_cards_list[i]:
                    sorted_cards_list.insert(i, card)
                    break
                elif i == len(sorted_cards_list)-1:
                    sorted_cards_list.append(card)
                    break

    winnings = []
    for i in range(len(sorted_cards_list)):
        #print(sorted_cards_list[i].cards, sorted_cards_list[i].type, "rank: ", i+1, "bid: ", sorted_cards_list[i].bid, "bid*rank: ", sorted_cards_list[i].get_bid_times_rank(i+1))
        winnings.append(sorted_cards_list[i].get_bid_times_rank(i+1))

    print(sum(winnings))

