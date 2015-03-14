import simplegui
import random

message = "Python is fun"
position = [50, 50]
width = 500
height = 500
interval = 2000

# Handler for text box
def update(text):
    global message
    message = text
    
# Handler for timer
def tick():
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x
    position[1] = y
    
def draw(canvas):
    canvas.draw_text(message,position,36,"Pink")
    
frame = simplegui.create_frame("Home",width,height)

text = frame.add_input("Message: ", update, 150)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

frame.start()
timer.start()
