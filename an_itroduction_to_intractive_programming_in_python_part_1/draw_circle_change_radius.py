"""draw circle with radius"""
import simplegui

size = 10
radius = 10

# Define event handler
def incr_button_handler():
    """Increment the size"""
    global size
    size = size + 1
    label.set_text("Value : "+str(size))
    
def decr_button_handler():
    """Decrement the size"""
    global size
    size = size - 1
    label.set_text("Value :"+str(size))
    
def change_circle_handler():
    """Change the circle radius"""
    global radius
    radius = size
    
def draw_handler(canvas):
    """Draw the circle"""
    canvas.draw_circle((100,100), radius, 5, "Red")
    
frame = simplegui.create_frame("Event_Handler",200,200)
label = frame.add_label("Value :"+str(size))
frame.add_button("Increase",incr_button_handler,150)
frame.add_button("Decrease",decr_button_handler,150)
frame.add_button("Change Circle",change_circle_handler,150)
frame.set_draw_handler(draw_handler)
frame.start()
