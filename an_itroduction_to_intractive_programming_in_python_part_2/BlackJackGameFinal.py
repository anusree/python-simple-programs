# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
in_play = True
score = 0
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
player_in_stand = False
game_over = False

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos, index=1):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
                    [pos[0] + CARD_CENTER[0] + 73 * index, 
                     pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
    def black_card_draw(self, canvas, pos, index=1):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, 
                    [pos[0] + CARD_BACK_CENTER[0] + 73 * index, 
                     pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)        
        
# define hand class
class Hand:
    def __init__(self, type='dealer'):
        # create Hand object
        self.card_list = []
        self.type = type

    def __str__(self):
        # return a string representation of a hand
        hand_obj_str = ""
        for i in self.card_list:
            hand_obj_str +=  str(i)
        return hand_obj_str

    def add_card(self, card):
        # add a card object to a hand
        self.card_list.append(card)
        
    def get_cards(self):
        return self.card_list

    def get_value(self):
        #print VALUES
        total = 0
        for val in self.card_list:
            k = val.get_rank()
            #print  "KEYS: ",k
            if k in VALUES:
                #print "VALUES: ",VALUES[k]
                total += VALUES[k]
        return total
            #print v
            #print "get_value() mthode: ",val
        
        
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for z in self.card_list:
            index = self.card_list.index(z)
            if index > 0 and self.type == 'dealer' and not player_in_stand:
                    z.black_card_draw(canvas, pos, index)
            else:
                z.draw(canvas, pos, index)
         
# define deck class 
class Deck:
    global SUITS, RANKS
    def __init__(self):
        # create a Deck object
        self.card_list = []
        for suits in SUITS:
            for ranks in RANKS:
                self.card_list.append(Card(str(suits),str(ranks)))

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.card_list)

    def deal_card(self):
        # deal a card object from the deck
        card = self.card_list.pop(0)
        return card
        
    def get_all_cards(self):
        return self.card_list
    
    def __str__(self):
        # return a string representing the deck
        str1 = "Deck contain "
        for i in self.card_list:
            str1 += str(i)
        return str1

#define event handlers for buttons
def deal():
    global player_hand, dealer_hand, deck, outcome, player_in_stand, game_over
    player_in_stand = False
    game_over = False
    deck = Deck()
    deck.shuffle()
    player_hand = Hand('player')
    dealer_hand = Hand('dealer')
    outcome = "Hit or Stand?"
    
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    #print "Player cards: ",[x.suit + x.rank for x in player_hand.get_cards()]
    #print "Player total score: ",player_hand.get_value()
    
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    #print "Dealer cards: ",[x.suit + x.rank for x in dealer_hand.get_cards()]
    #print "Number of cards in he deck: ", len(deck.get_all_cards())
    #print "Dealer total score: ",dealer_hand.get_value()


def hit():
    # replace with your code below
    global player_hand, score, outcome, game_over
    if game_over:
        return True
    
    if player_hand.get_value() < 21:
        
        player_hand.add_card(deck.deal_card())
        #print "Player cards: ",[x.suit + x.rank for x in player_hand.get_cards()]
        #print "Player total score: ",player_hand.get_value()
        #score -= 1
    if player_hand.get_value() > 21:
        outcome = "Player busts, Player Lost, New deal?"
        game_over = True
        score -= 1
        
    

    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # replace with your code below
    global dealer_hand, outcome, score, player_in_stand, game_over
    #print "Stand button: ",dealer_hand
    #print "Stand button"
    player_in_stand = True
    if player_hand.get_value() > 21:
        outcome = "Player busts, Player Lost, New deal?"
        game_over = True
        score -= 1
        
    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        else:
            if dealer_hand.get_value() > 21:
                outcome = "Dealer busts, Player win, New deal?"
                game_over = True
                score += 1
                
            elif dealer_hand.get_value() >= player_hand.get_value():
                outcome = "Player Lost. New deal?"
                game_over = True
                score -= 1
                
            else:
                outcome = "Player Win, New deal?"
                game_over = True
                score += 1
   
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome, player_hand, dealer_hand

    dealer_hand.draw(canvas, [100, 180])
    player_hand.draw(canvas, [100, 450])
    
    canvas.draw_text("BlackJack",[150,50],40,"Pink")
    canvas.draw_text("Score: ",[450,50],25,"Black")
    canvas.draw_text(str(score),[540,50],25,"Black")
    canvas.draw_text("Dealer ",[100,150],25,"Black") 
    canvas.draw_text("Player ",[100,420],25,"Black")
    canvas.draw_text(outcome,[230,420],20,"Black")
    canvas.draw_text("Player Hand: "+str(player_hand.get_value()), [230,580], 20, "Black")
    
    
    
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 680, 650)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric