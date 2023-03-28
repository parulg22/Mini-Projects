#Teach python how to play poker and award points to players  

import random
import sys

class Card (object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    SUITS = ('C', 'D', 'H', 'S')

    #constructor 
    def __init__(self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS):
            self.rank = rank 
        else:
            self.rank = 12
        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    # string representation of a Card object
    def __str__(self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str(self.rank)
        return rank + self.suit

    # equality tests 
    def __eq__ (self, other):
        return self.rank == other.rank

    def __ne__ (self, other):
        return self.rank != other.rank

    def __lt__ (self, other):
        return self.rank < other.rank

    def __le__ (self, other):
        return self.rank <= other.rank

    def __gt__ (self, other):
        return self.rank > other.rank

    def __ge__ (self, other):
        return self.rank >= other.rank

class Deck(object):
    # constructor
    def __init__(self, num_decks = 1):
        self.deck =[]
        for i in range(num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card(rank, suit)
                    self.deck.append(card)

    # shuffle the deck
    def shuffle (self):
        random.shuffle(self.deck)

    # deal a card
    def deal (self):
        if len(self.deck) == 0:
            return None # do nothing 
        else:
            return self.deck.pop(0) # take out the first card and give it back 

class Poker(object):
    # constructor
    def __init__(self, num_players = 2, num_cards = 5):
        # create the deck object
        self.deck = Deck()
        # shuffle the deck
        self.deck.shuffle()
        # list of hands of all players
        self.players_hands=[]
        # how many cards are in a hand
        self.numCards_in_Hand = num_cards 

    # deal all the cards
        for i in range(num_players):
            hand = []
            for j in range(self.numCards_in_Hand):
                hand.append(self.deck.deal())
            self.players_hands.append(hand)

    # simulate the play of the game
    def play(self):
        # sort the hands of each player and print
        for i in range(len(self.players_hands)):
            # takes each hand and sorts it
            # we told python how to sort it: given 2 cards, this is the relationship that they 
            # have between them 
            # using 6 functions written above 
            sorted_hand = sorted(self.players_hands[i], reverse = True)
            self.players_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Player ' + str(i + 1) + ' : ' + hand_str)
        print()
        # create list of all hands of all players 
        # create list of all points of all players 
        hand_lst = []
        pts_lst = []
        for i in range(len(self.players_hands)):
            # calculate_score returns a tuple of (points, string)
            calc_points = self.calculate_score(self.players_hands[i])
            hand_lst.append(calc_points[1])
            pts_lst.append(calc_points[0])
        # sort point list in descending order and find max 
        highest_scores = sorted(pts_lst, reverse = True)
        max_pts = highest_scores[0]
        # getting hand associated with max points
        # # win_str is used to determine the tie 
        win_str = ""
        for i in range(len(hand_lst)):
            if(pts_lst[i] == max_pts):
                win_str = hand_lst[i]
        for i in range(len(self.players_hands)):
            print('Player ' + str(i + 1) + ': ' + hand_lst[i])
        print()
        # create a list of all winners
        winners_lst = []
        for i in range(len(hand_lst)):
            if hand_lst[i] == win_str:
                winners_lst.append(i+1)
        # check winners list length to see if there's a tie
        # print ties in descending order of points
        if len(winners_lst) > 1:
            for i in range(len(winners_lst)):
                most_points = highest_scores[i]
                for j in range(len(pts_lst)):
                    if(pts_lst[j] == most_points):
                        print('Player ' + str(j+1) + ' ties.')    
                        break           
        else:
            print('Player ' + str(winners_lst[0]) + ' wins.')
        

    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card Objects 
    # returns a number of points for that hand 
    def is_royal(self,hand):
        same_suit = True
        for i in range(len(hand)-1):
            same_suit = same_suit and (hand[i].suit == hand[i+1].suit)
        if (not same_suit):
            return 0, '' # blank string indicates you don't know what hand is right now 
        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)
        if (not rank_order):
            return 0, ''
        # determine the points
        points = 10 * 15**5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15**3 \
                 + (hand[2].rank) * 15**2 + (hand[3].rank) * 15**1 \
                 + hand[4].rank
        return points, 'Royal Flush'

    # determine if a hand is a straight flush
    # takes as argument a list of 5 Card Objects 
    # returns a number of points for that hand 
    def  is_straight_flush(self, hand):
        same_suit = True
        for i in range(len(hand)-1):
            same_suit = same_suit and (hand[i].suit == hand[i+1].suit)
        if (not same_suit):
            return 0, '' # blank string indicates you don't know what hand is right now 
        rank_order = True
        # how to find rank of high card 
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == hand[0].rank - i)

        if (not rank_order):
            return 0, ''

        points = 9 * 15**5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15**3 \
                 + (hand[2].rank) * 15**2 + (hand[3].rank) * 15**1 
        return points, 'Straight Flush'

    # determine if a hand is four of a kind
    # takes as argument a list of 5 Card Objects 
    # returns a number of points for that hand 
    def is_four_kind(self, hand):
        if (hand[0].rank == hand[1].rank == hand[2].rank == hand[3].rank):
            return ((8 * 15**5 + hand[0].rank * 15**4 + hand[1].rank * 15**3 + hand[2].rank * 15**2 \
                     + hand[3].rank * 15 + hand[4].rank), 'Four of a Kind')
        elif (hand[1].rank == hand[2].rank == hand[3].rank == hand[4].rank):
            return ((8 * 15**5 + hand[1].rank * 15**4 + hand[2].rank * 15**3 + hand[3].rank * 15**2 \
                    + hand[4].rank * 15 + hand[0].rank), 'Four of a Kind')
        else:
            return 0, ''

    # determine if a hand is a full house 
    # takes as argument a list of 5 Card Objects 
    # returns a number of points for that hand 
    def is_full_house(self, hand):
        if (hand[0].rank == hand[1].rank == hand[2].rank) and (hand[3].rank == hand[4].rank):
            return ((7 * 15**5 + hand[0].rank * 15**4 + hand[1].rank * 15**3 + hand[2].rank * 15**2 \
                   + hand[3].rank * 15 + hand[4].rank), 'Full House')
        elif (hand[0].rank == hand[1].rank) and (hand[2].rank == hand[3].rank == hand[4].rank):
            return ((7 * 15**5 + hand[2].rank * 15**4 + hand[3].rank * 15**3 + hand[4].rank * 15**2 \
                   + hand[0].rank * 15 + hand[1].rank), 'Full House')
        else: 
            return 0, ''

    # determine if a hand is a flush
    # takes as argument a list of 5 Card Objects 
    # returns a number of points for that hand 
    def is_flush(self, hand):
        same_suit = True
        for i in range(len(hand)-1):
            same_suit = same_suit and (hand[i].suit == hand[i+1].suit)
        if (not same_suit):
            return 0, '' # blank string indicates you don't know what hand is right now 
        points = 6 * 15**5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15**3 \
                 + (hand[2].rank) * 15**2 + (hand[3].rank) * 15**1 \
                 + hand[4].rank
        return points, 'Flush'

    # determine if a hand is straight
    # takes as argument a list of 5 Card Objects 
    # returns a number of points for that hand 
    def is_straight (self, hand):
        rank_order = True   
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == hand[0].rank - i)

        if (not rank_order):
            return 0, ''

        points = 5 * 15**5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15**3 \
                 + (hand[2].rank) * 15**2 + (hand[3].rank) * 15**1 \
                 + hand[4].rank
        return points, 'Straight'

    # determine if a hand is three of a kind 
    # takes as argument a list of 5 Card Objects 
    # returns a number of points for that hand 
    def is_three_kind(self, hand):
        three_straight = False 
        counter = 1
        indices_set = set()
        for i in range(len(hand)-1):
            if hand[i].rank == hand[i+1].rank:
                counter += 1
                indices_set.add(i)
                indices_set.add(i+1)
            else:
                counter = 1
                indices_set.clear()
            if counter >= 3:
                three_straight = True 
                break
        if (not three_straight):
            return 0, '' # blank string indicates you don't know what hand is right now 
        
        hand_set = set([0,1,2,3,4])
        not_in_three = hand_set.symmetric_difference(indices_set)

        points = 4 * 15**5 + (hand[indices_set.pop()].rank) * 15 ** 4 + (hand[indices_set.pop()].rank) * 15**3 \
                 + (hand[indices_set.pop()].rank) * 15**2 + (hand[min(not_in_three)].rank) * 15**1 \
                 + hand[max(not_in_three)].rank
        return points, 'Three of a Kind'

    # determine if a hand has two pairs 
    # takes as argument a list of 5 Card Objects 
    # returns a number of points for that hand 
    def is_two_pair(self, hand):
        two_pair = False
        counter = 0 
        indices_list = []
        for i in range(len(hand)-1):
            if hand[i].rank == hand[i+1].rank:
                counter += 1
                indices_list.append(i)
        if counter >= 2:
            two_pair = True 
        if (not two_pair):
            return 0, '' # blank string indicates you don't know what hand is right now 
        c5_index = {0,1,2,3,4}.symmetric_difference({indices_list[0], indices_list[0]+1, indices_list[1], indices_list[1]+1})
        # change c5_index from set to integer by popping the only value in the set 
        c5_index = c5_index.pop()
        points = 3 * 15**5 + (hand[indices_list[0]].rank) * 15 ** 4 + (hand[indices_list[0]].rank) * 15**3 \
                 + (hand[indices_list[1]].rank) * 15**2 + (hand[indices_list[1]].rank) * 15**1 \
                 + hand[c5_index].rank
        return points, 'Two Pair'        

    # determine if a hand has one pair 
    # takes as argument a list of 5 Card Objects 
    # returns a number of points for that hand 
    def is_one_pair(self, hand):
        one_pair = False 
        indices_set = set()
        for i in range(len(hand)-1):
            if hand[i].rank == hand[i+1].rank:
                one_pair = True 
                indices_set.add(i)
                indices_set.add(i+1)
                break
        if (not one_pair):
            return 0, '' # blank string indicates you don't know what hand is right now 
        # find indices of pairs and not pairs to eventually assign points to index 
        not_pair = {0,1,2,3,4}.symmetric_difference(indices_set)
        c3 = min(not_pair)
        not_pair.remove(min(not_pair))
        c4 = min(not_pair)
        not_pair.remove(min(not_pair))
        c5 = not_pair.pop()
        points = 2 * 15**5 + (hand[indices_set.pop()].rank) * 15 ** 4 + (hand[indices_set.pop()].rank) * 15**3 \
                 + (hand[c3].rank) * 15**2 + (hand[c4].rank) * 15**1 \
                 + hand[c5].rank
        return points, 'One Pair'

    # determine if a hand is a high card
    # takes as argument a list of 5 Card Objects 
    # returns a number of points for that hand 
    def is_high_card(self, hand):
        # points to award 
        return((1 * 15**5 + hand[0].rank * 15**4 + hand[1].rank * 15**3 + hand[2].rank * 15**2 + \
               hand[3].rank * 15 + hand[4].rank), 'High Card')

# calculate the score for a player by returning appropriate hand and points 
    def calculate_score(self, hand):
        if self.is_royal(hand) != (0, ''):
            return self.is_royal(hand)
        elif self.is_straight_flush(hand) != (0, ''):
            return self.is_straight_flush(hand)
        elif self.is_four_kind(hand) != (0, ''):
            return self.is_four_kind(hand)
        elif self.is_full_house(hand)!= (0, ''):
            return self.is_full_house(hand)
        elif self.is_flush(hand)!= (0, ''):
            return self.is_flush(hand)
        elif self.is_straight(hand)!= (0, ''):
            return self.is_straight(hand)
        elif self.is_three_kind(hand)!= (0, ''):
            return self.is_three_kind(hand)
        elif self.is_two_pair(hand)!= (0, ''):
            return self.is_two_pair(hand)
        elif self.is_one_pair(hand)!= (0, ''):
            return self.is_one_pair(hand)
        else:
            return self.is_high_card(hand)

def main():
    # read number of players from stdin
    line = sys.stdin.readline()
    line = line.strip()
    num_players = int(line)
    if (num_players<2) or (num_players > 6):
        return

    # create the Poker object 
    game = Poker(num_players)

    # play the game
    game.play()

if __name__ == "__main__":
    main()    


