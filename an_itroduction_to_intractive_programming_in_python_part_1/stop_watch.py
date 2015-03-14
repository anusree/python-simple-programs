# template for "Stopwatch: The Game"

# define global variables
import simplegui
NUMBER_TENTH_OF_SEC = 0
COUNT_TOTAL_STOP = 0
COUNT_SUCCESFUL_STOP = 0
IS_RUNNING = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(num_tenth_sec):
    a = num_tenth_sec//600
    b = ((num_tenth_sec//10)%60)//10
    c = ((num_tenth_sec//10)%60)%10
    d = num_tenth_sec%10
    return "%s:%s%s.%s" %(a,b,c,d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    global IS_RUNNING
    IS_RUNNING = True
    timer.start()

def stop_button():
    global COUNT_TOTAL_STOP, COUNT_SUCCESFUL_STOP, IS_RUNNING
    timer.stop()
    if IS_RUNNING == True:
        COUNT_TOTAL_STOP += 1
        if NUMBER_TENTH_OF_SEC%10 == 0:
            COUNT_SUCCESFUL_STOP += 1
    IS_RUNNING = False

def reset_button():
    global NUMBER_TENTH_OF_SEC, IS_RUNNING
    global COUNT_TOTAL_STOP, COUNT_SUCCESFUL_STOP
    IS_RUNNING = False
    timer.stop()
    NUMBER_TENTH_OF_SEC = 0
    COUNT_TOTAL_STOP = 0
    COUNT_SUCCESFUL_STOP = 0

def timer_handler():
    global NUMBER_TENTH_OF_SEC
    NUMBER_TENTH_OF_SEC = NUMBER_TENTH_OF_SEC + 1
    #print NUMBER_TENTH_OF_SEC

timer = simplegui.create_timer(100, timer_handler)

# define event handler for timer with 0.1 sec interval


# define draw handler

def draw(canvas):
    canvas.draw_text(format(NUMBER_TENTH_OF_SEC), [70,150], 60, "White") 
    canvas.draw_text(str(COUNT_SUCCESFUL_STOP)+"/"+str(COUNT_TOTAL_STOP),[260,50],20,"Green")
# create frame
frame = simplegui.create_frame("Stop Watch",300,300)

# register event handlers
button1 = frame.add_button('Start', start_button,150)
button2 = frame.add_button('Stop', stop_button,150)
button3 = frame.add_button('reset', reset_button,150)
frame.set_draw_handler(draw)

# start frame
frame.start()
# Please remember to review the grading rubric

