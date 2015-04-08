# implementation of card game - Memory

import simplegui
import random

clicked_indexes = []
turns = 0
# helper function to initialize globals
def new_game():
    global exposed, add_list, turns
    list1 = []
    for i in range(8):
        list1.append(i)

    list2 = []
    for j in range(8):
        list2.append(j)
       
    add_list = list1 + list2
    random.shuffle(add_list)
    
    
    exposed=[False,False,False,False,False,False,False,False,  
         False,False,False,False,False,False,False,False]  
    turns = 0
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed,add_list,clicked_indexes,turns
    index = pos[0]/50
    if exposed[index] == False:
        exposed[index] = True
    
        if len(clicked_indexes) == 0 or len(clicked_indexes) < 3:
            clicked_indexes.append(index)
     
        if len(clicked_indexes) == 3:
            if add_list[clicked_indexes[0]] != add_list[clicked_indexes[1]]:
                exposed[clicked_indexes[0]] = False         
                exposed[clicked_indexes[1]] = False
                turns += 1 
            clicked_indexes = [index]
           
  
# cards are logically 50x100 pixels in size    
def draw(canvas):
   
    poly_x_value = 0
   
    distance = 20
    for i in add_list:
        label.set_text("Turns = "+str(turns)) 
        canvas.draw_line((50, 0), (50, 100), 5, 'Red')
        canvas.draw_line((100, 0), (100, 100), 5, 'Red')
        canvas.draw_line((150, 0), (150, 100), 5, 'Red')
        canvas.draw_line((200, 0), (200, 100), 5, 'Red')
        canvas.draw_line((250, 0), (250, 100), 5, 'Red')
        canvas.draw_line((300, 0), (300, 100), 5, 'Red')
        canvas.draw_line((350, 0), (350, 100), 5, 'Red')
        canvas.draw_line((400, 0), (400, 100), 5, 'Red')
        canvas.draw_line((450, 0), (450, 100), 5, 'Red')
        canvas.draw_line((500, 0), (500, 100), 5, 'Red')
        canvas.draw_line((550, 0), (550, 100), 5, 'Red')
        canvas.draw_line((600, 0), (600, 100), 5, 'Red')
        canvas.draw_line((650, 0), (650, 100), 5, 'Red')
        canvas.draw_line((700, 0), (700, 100), 5, 'Red')
        canvas.draw_line((750, 0), (750, 100), 5, 'Red')
        canvas.draw_text(str(i), [(0+distance) , 50], 30, 'Pink')
        distance +=50
        #print "-----",poly_x_value
        index_of_card = poly_x_value / 50
        if exposed[index_of_card] == False:
            canvas.draw_polygon([(poly_x_value, 0), (poly_x_value, 100),  
                                 (poly_x_value+50, 100),(poly_x_value+50, 0)],  
                                1, "Green", "Green")
        
        poly_x_value += 50
    
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric