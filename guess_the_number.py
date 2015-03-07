# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
NUM_GUESS = 7
TEMP_NUM_GUESS = NUM_GUESS
#print TEMP_NUM_GUESS
RANGE_TO = 100

#COMPUTER_GUESS = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global NUM_GUESS,RANGE_TO,TEMP_NUM_GUESS
    #GUESS100 = 7
    global COMPUTER_GUESS 
    TEMP_NUM_GUESS = NUM_GUESS
    print ""
    print "New game range from 0,",RANGE_TO
    print "Number of remaining guesses is",NUM_GUESS
    COMPUTER_GUESS = random.randrange(0,RANGE_TO+1)
    #print "COMPUTER_GUESS  ",COMPUTER_GUESS

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global RANGE_TO
    global NUM_GUESS
    NUM_GUESS = 7
    RANGE_TO = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global NUM_GUESS, RANGE_TO
    NUM_GUESS = 10
    RANGE_TO = 1000
    new_game()
     
def input_guess(guess):
    global TEMP_NUM_GUESS
    TEMP_NUM_GUESS = TEMP_NUM_GUESS - 1
    guess_num = int(guess)
    print ""
    print "Guess was",guess_num
    print "Number of remaining guesses is",TEMP_NUM_GUESS

    if COMPUTER_GUESS > guess_num:
        print "Higher!"
        #print COMPUTER_GUESS, guess_num

    elif COMPUTER_GUESS < guess_num:
        print "Lower!"
        #print COMPUTER_GUESS, guess_num
    else:
        print "Correct!"
        new_game()
        
    if TEMP_NUM_GUESS <= 0:
        #print "Guess was",guess_num
        #print "Number of remaining guesses is",TEMP_NUM_GUESS
        print "You ran out of guesses. The number was",COMPUTER_GUESS
        new_game()        
    # main game logic goes here	
    
# create frame
frame = simplegui.create_frame("Guess the Number",200,200)
frame.add_button("Range is[0, 100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)
frame.add_input("Enter a guess",input_guess,200)

# register event handlers for control elements and start frame

frame.start()
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
