# import openai
import pygame
from pygame import mixer
import os

"""
Solar System Shit
Brick Breaker
225 MPs/Labs
Build a perceptron dude
Build a sorting visualizer



computer vision for league pro play / script detector
plugin identifier in songs?
ping pong ml bot
ai nerf gun dececting shoot / sentry unit type sht
common app essay ai reviewer/tutor 

"""


song = os.path.join("sounds", "forward.mp3")

mixer.init() 
mixer.music.load(song) 
mixer.music.set_volume(0.7) 
mixer.music.play(-1, 1.0) 

background_colour = (234, 212, 252) 
rectangle_color = (255,0,0) # red baby
  
screen = pygame.display.set_mode((800, 400)) 
  

pygame.display.set_caption('sort_algo') 

# Fill the background colour to the screen 
screen.fill(background_colour)


class Rect:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

        self.rect = None
        self.outline = None

class RectList:
    def __init__(self):
        self.list = []# full of rects

    def append(self, rect):
        self.list.append(rect)
    
    def print_list(self):
        index = 0
        for block in self.list:
            print("rect " + str(index) + ": " + str(block.left) + " " + str(block.top) + " " + str(block.width) + " " + str(block.height))
            index += 1

    def index(self, obj):
        index = 0
        for block in self.list:
            if block == obj:
                return index
            index += 1;

        

def draw_rectangles(number): 
    divider = int(screen.get_width() / number)
    dividerh = int(screen.get_height() / number)
    # print(screen.get_width(), divider)
    for i in range(0,800,divider): #increment by divider
        # outline = rect.inflate(rect.width*2, rect.width*2)
        left = 0 + i
        top = screen.get_height()-(dividerh*(i / divider))
        width = screen.get_width()/number
        height = screen.get_height()-top
        if i == 0: #first block
            top -= 5
    
        rect_outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left-1, top - 1, width + 1, height+2))
        rect = pygame.draw.rect(screen, rectangle_color, pygame.Rect(left, top, width, height))

        block = Rect(left, top, width, height)
        block.rect = rect
        block.outline = rect_outline

        rectlist.append(block)

    rectlist.print_list()
    return rectlist

def drawRect(rect):
    left = rect.left
    top = rect.top
    width = rect.width  
    height = rect.height
    rect_outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left-1, top - 1, width + 1, height+2))
    rect = pygame.draw.rect(screen, rectangle_color, pygame.Rect(left, top, width, height))

def deleteRect(rect): #delete rectangle from pygame canvas
    pass

def swap_rectangles(rect1, rect2):
    """just switch left,top,width,andheight for rects and draw them again
       also switch order of rectangles in the list
    """
    rect1_index = rectlist.index(rect1)
    rect2_index = rectlist.index(rect2)

    rectlist.list[rect1_index] = rect2
    rectlist.list[rect2_index] = rect1

    tmp = rect1
    rect1 = rect2
    rect2 = rect1

    
    

    
""""
DEBUG


how do we add 1 to the height for the first rectangle

and need to implement sort still


DEBUG
"""
rectlist = RectList()
draw_rectangles(20)

rect1 = rectlist.list[0]
rect2 = rectlist.list[4]

swap_rectangles(rect1, rect2)



# Update the display using flip 
pygame.display.flip() 
  
# Variable to keep our game loop running 
running = True
  
# game loop 
while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False


