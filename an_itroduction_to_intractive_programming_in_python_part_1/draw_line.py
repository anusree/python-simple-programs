"""
Assume we have a canvas that is 200 pixels wide and 300 pixels high. We want to draw a green line between the upper left corner and the lower right corner
"""

import simplegui

#define draw_handler
def draw(canvas):
    #canvas.draw_text(str(value), [200, 300], 24, "Pink")
    #canvas.draw_line((0, 0), (299, 199), 10, "Green")
    #canvas.draw_line((299, 0), (0, 199), 10, "Green")
    canvas.draw_line((199, 299), (0, 0), 10, "Green")

#create frame
frame = simplegui.create_frame("Dollor to cent", 200, 300)

#register event handler
frame.set_draw_handler(draw)

#start the frame
frame.start()

