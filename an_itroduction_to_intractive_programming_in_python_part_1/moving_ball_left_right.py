import simplegui

WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-40.0/60.0, 5.0/60.0]
#time = 0

#def tick():
#    global time
#    time +=1

def draw(canvas):
    #ball_pos = [0, 0]
    
    #ball_pos[0] = init_pos[0] + time * vel[0]
    #ball_pos[1] = init_pos[1] + time * vel[1]
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    if ball_pos[0] <=BALL_RADIUS:
        vel[0] = -vel[0]
    elif ball_pos[0] >=(WIDTH-1)-BALL_RADIUS:
        vel[0] = -vel[0]
    
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    

frame = simplegui.create_frame("Positional ball control", WIDTH, HEIGHT)

frame.set_draw_handler(draw)
#timer = simplegui.create_timer(100, tick)

#timer.start()
frame.start()
