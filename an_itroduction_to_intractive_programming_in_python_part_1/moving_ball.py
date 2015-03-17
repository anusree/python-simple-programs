import simplegui

WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]

def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
def keydown(key):
    vel = 4
    if key == simplegui.KEY_MAP["left"]:
        ball_pos[0] -= vel
    if key == simplegui.KEY_MAP["right"]:
        ball_pos[0] += vel
    if key == simplegui.KEY_MAP["down"]:
        ball_pos[1] += vel
    if key == simplegui.KEY_MAP["up"]:
        ball_pos[1] -= vel
        
frame = simplegui.create_frame("Positional ball control", WIDTH, HEIGHT)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

frame.start()
