import simplegui
import random



# Global Constant
WIDTH = 600
HEIGHT = 400
PARTICLE_RADIUS = 5
COLOR_LIST = ["Red", "Green", "Blue", "White", "Pink", "Yellow", "Indigo", "Orange", "Gray", "Amaranth"]
DIRECTION_LIST = [[1, 0], [0, 1], [-1, 0], [0, -1]]


# Definition of particle class
class Particle:
    # initializer for particle
    def __init__(self, position, color):
        self.position = position
        self.color = color
        
        
        
    # methode that updates position of particle
    def move(self, offset):
        self.position[0] += offset[0]
        self.position[1] += offset[1]
        
    # draw method for particle
    def draw(self, canvas):
        #canvas.draw_circle(self.position, PARTICLE_RADIUS,1,random.choice(COLOR_LIST))
        canvas.draw_circle(self.position, PARTICLE_RADIUS,1,self.color,self.color)
    # starting methode for particle
    def __str__(self):
        return "Particle with position = "+str(self.position)
        
# draw handler
def draw(canvas):
    for p in particle_list:
        p.move(random.choice(DIRECTION_LIST))
        
    for p in particle_list:
        p.draw(canvas) 
        
# create a frame and register draw handler
frame = simplegui.create_frame("Particle simulator", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# create a list of particle
particle_list = []
for i in range(50):
    p = Particle([WIDTH / 2, HEIGHT / 2], random.choice(COLOR_LIST))
    particle_list.append(p)
    print p

# start the frame
frame.start()
