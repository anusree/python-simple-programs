import simplegui
import math

WIDTH = 450
HEIGHT = 300
ball_pos = [WIDTH/2, HEIGHT/2]
BALL_RADIUS = 15
ball_color  = "Red"





def distance(p, q):
    return math.sqrt( (p[0] - q[0]) **2 + (p[1] - q[1])**2)


def click(pos):
    global ball_pos,ball_color
    print pos
    if distance(pos,ball_pos) < BALL_RADIUS:
        ball_color = "Green"
    else:   
        ball_pos = list(pos)
        ball_color = "Red"

def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Black", ball_color)


frame = simplegui.create_frame("Mouse Secection", WIDTH, HEIGHT)
frame.set_canvas_background("Pink")


frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

frame.start()
