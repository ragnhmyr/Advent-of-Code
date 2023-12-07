file_name = '7_input.txt'

#from lowest to highest
card_strength = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
hand_type = ["high-card", "one-pair", "two-pairs", "three-of-a-kind", "full-house", "four-of-a-kind", "five-of-a-kind"]

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.type = self.get_hand_type()

    def get_hand_type(self):
        set_cards = set(self.cards)
        length_set_cards = len(set_cards)
        if length_set_cards == 5:
            return "high-card"
        elif length_set_cards == 1:
            return "five-of-a-kind"
        elif length_set_cards == 4:
            return "one-pair"
        elif length_set_cards == 2: #can be four of a kind or full house
            #counting the first string occurence to see if it is four of a kind or full house
            first_character_count = self.cards.count(self.cards[0])
            if first_character_count == 4 or first_character_count == 1:
                return "four-of-a-kind"
            else:
                return "full-house"
        else: 
            #then length_set_cards = 3 and that can be either three of a kind or two pairs 
            #creating a dict with the number of occurences of each card
            res = {i: self.cards.count(i) for i in set_cards}
            #if any of the occurernces is 3 then it is three of a kind, else it is two pairs
            if (3 in res.values()):
                return "three-of-a-kind"
            else:
                return "two-pairs"   

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
        print(sorted_cards_list[i].cards, sorted_cards_list[i].type, "rank: ", i+1, "bid: ", sorted_cards_list[i].bid, "bid*rank: ", sorted_cards_list[i].get_bid_times_rank(i+1))
        winnings.append(sorted_cards_list[i].get_bid_times_rank(i+1))

    print(sum(winnings))

