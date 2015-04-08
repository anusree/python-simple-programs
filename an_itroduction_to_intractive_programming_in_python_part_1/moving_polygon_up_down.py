import simplegui

paddle_x = 180
paddle_y = 30
right_paddle = [paddle_x,paddle_y]

def draw_handler(canvas):
    global paddle_x,paddle_y, right_paddle
    canvas.draw_polygon([(right_paddle[0],right_paddle[1]), (right_paddle[0]+2,right_paddle[1]), (right_paddle[0]+2,right_paddle[1]+30), (right_paddle[0],right_paddle[1]+30)], 12, 'Green')
    

def keydown(key):
    
    vel = 4
    #if key == simplegui.KEY_MAP["left"]:
        #right_paddle[0] -= vel
        #print right_paddle[0]
    #if key == simplegui.KEY_MAP["right"]:
        #right_paddle[0] += vel
        #print right_paddle[0]
    if key == simplegui.KEY_MAP["down"]:
        right_paddle[1] += vel
        print right_paddle[1]
    if key == simplegui.KEY_MAP["up"]:
        right_paddle[1] -= vel
        print right_paddle[1]


frame = simplegui.create_frame('Testing', 200, 200)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(keydown)
frame.start()
