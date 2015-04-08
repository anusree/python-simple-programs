# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [-40.0/60.0, 5.0/60.0]
SCORE_LEFT = 0
SCORE_RIGHT = 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, SCORE_LEFT, SCORE_RIGHT # these are vectors stored as lists
    #satrt ball from the center
    ball_pos = [WIDTH/2, HEIGHT/2]
    
    if direction == False:
        ball_vel[0] = 40.0/60.0
        SCORE_RIGHT += 1
        #print "Ball Collied outside the Left Paddle"
    if direction ==True:
        ball_vel[0] = -40.0/60.0
        SCORE_LEFT += 1
        #print "Ball Collied outside the Right Paddle"
# define event handlers
def new_game():
    global paddle_left_pos, paddle_right_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, ball_pos  # these are ints    
    paddle_left_pos = [PAD_WIDTH / 2, HEIGHT / 2]
    paddle_right_pos = [WIDTH - PAD_WIDTH / 2, HEIGHT / 2]
    ball_pos = [WIDTH/2, HEIGHT/2]
    paddle1_vel = 0
    paddle2_vel = 0
    
def button_handler():
    global SCORE_LEFT, SCORE_RIGHT
    SCORE_LEFT = 0
    SCORE_RIGHT = 0
    new_game()

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,SCORE_LEFT, SCORE_RIGHT
    global paddle_left_pos, paddle_right_pos, pad_left_bottom, pad_left_top, pad_right_bottom, pad_right_top
    string_score_left = str(SCORE_LEFT)
    string_score_right = str(SCORE_RIGHT)
    ####Draw MidLine and Gutters####
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
          
    ####Update Ball Position####
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]        
    ##Draw ball##
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    #print "DRAW", SCORE_LEFT, SCORE_RIGHT
    ####Draw Paddles####
    ##Draw Left Paddle##
    #Left Paddle top point
    pad_left_top = [paddle_left_pos[0], paddle_left_pos[1] - HALF_PAD_HEIGHT]
    #Left Paddle bottom point
    pad_left_bottom = [paddle_left_pos[0], paddle_left_pos[1] + HALF_PAD_HEIGHT]
    canvas.draw_line(pad_left_top, pad_left_bottom, PAD_WIDTH, "White")
    
    ##Draw Right Paddle##
    #Right Paddle top point
    pad_right_top = [paddle_right_pos[0], paddle_right_pos[1] - HALF_PAD_HEIGHT]
    #Right Paddle bottom point
    pad_right_bottom  = [paddle_right_pos[0], paddle_right_pos[1] + HALF_PAD_HEIGHT]
    canvas.draw_line(pad_right_top, pad_right_bottom, PAD_WIDTH, "White")   
    
    ##Determine whether the ball is collied on top and bottom of the frame
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    if ball_pos[1] >= (HEIGHT - 1 - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    
    
    ####Determine whether paddle and ball collide####
    ##Determine whether Left Paddle and ball collide##
    new_left_paddle_width_x = PAD_WIDTH + BALL_RADIUS
    new_left_paddle_top_point_y = pad_left_top[1]
    new_left_paddle_bottom_point_y = pad_left_bottom[1]
    if ball_pos[0] <= new_left_paddle_width_x and  ball_pos[1] >= new_left_paddle_top_point_y and ball_pos[1] <= new_left_paddle_bottom_point_y:
        #IF ball collide with Left Paddle
        #Increase the x velocity to .1 to move the ball fast towards to right side
        ball_vel[0] = -ball_vel[0] + .1
    elif ball_pos[0] <= new_left_paddle_width_x and (ball_pos[1] < new_left_paddle_top_point_y or ball_pos[1] > new_left_paddle_bottom_point_y):
        #IF ball collide outside the Left Paddle. Tips: use 'or' condition to check 'y' of paddiles endpoints and use parenthesis '()' around them.
        spawn_ball(LEFT)
    
    ##Determine whether Right Paddle and ball collide##
    new_right_paddle_x = WIDTH - PAD_WIDTH - BALL_RADIUS
    new_right_paddle_top_point_y = pad_right_top[1]
    new_right_paddle_bottom_point_y = pad_right_bottom[1]
    if ball_pos[0] >= new_right_paddle_x and(ball_pos[1]>= new_right_paddle_top_point_y and ball_pos[1] <= new_right_paddle_bottom_point_y ):
            #IF ball collide with Right Paddle
            #Decrease the x velocity to .1 to move the ball fast towards to right side
            ball_vel[0] = -ball_vel[0] + -.1
    elif ball_pos[0] >= new_right_paddle_x and ((ball_pos[1]< new_right_paddle_top_point_y) or (ball_pos[1] > new_right_paddle_bottom_point_y )):
            spawn_ball(RIGHT)
    
    ####Draw scores####
    canvas.draw_text(string_score_left, (145,50), 50, "White")
    canvas.draw_text(string_score_right, (445,50), 50, "White")

def keydown(key):
    global paddle1_vel, paddle2_vel, paddle_left_pos, paddle_right_pos
    paddle1_vel = 20
    paddle2_vel = 20
    ####For Right Paddle####
    if key == simplegui.KEY_MAP["down"]:
        ##Right Paddle moves only up to right bottom corner of the frame
        if pad_right_bottom[1]+paddle2_vel <= 400:
            paddle_right_pos[1] += paddle1_vel
            #print paddle_right_pos[1]
    
       
    ####For Left Paddle####
    if key == simplegui.KEY_MAP["s"]:
        ##Left Paddle moves only up to left bottom corner of the frame
        if pad_left_bottom[1]+paddle2_vel <= 400:
            paddle_left_pos[1] += paddle2_vel
            #print paddle_left_pos[1]
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["up"]:
        ##Right Paddle moves only up to right top corner of the frame
        if pad_right_top[1]-paddle2_vel >= 0:
            paddle_right_pos[1] -= paddle1_vel
            #print paddle_right_pos[1]
    
    if key == simplegui.KEY_MAP["w"]:
        ##Left Paddle moves only up to left top corner of the frame
        if pad_left_top[1]-paddle2_vel >= 0:
            paddle_left_pos[1] -= paddle2_vel
            #print paddle_left_pos[1] 
   

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
###Add restart button####
button1 = frame.add_button('Restart', button_handler)

# start frame
new_game()
frame.start()

