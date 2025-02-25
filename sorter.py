# import openai
import pygame
from pygame import mixer
import os
import copy
import random

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

background_colour = (0,0,0) 
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

    def insert(self, index):
        pass

    def __getitem__(self, index):
        return self.list[index]  # Allow indexing like a regular list

    def __setitem__(self, index, value):
        self.list[index] = value  # Allow setting items at an index

    def __repr__(self):
        return f"RectList({self.list})"

        

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
        # if i == 0: #first block
        #     top -= 5
    
        # rect_outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left-.5, top - .5, width + .5, height+1))
        rect = pygame.draw.rect(screen, rectangle_color, pygame.Rect(left, top, width, height))

        block = Rect(left, top, width, height)
        block.rect = rect
        # block.outline = rect_outline

        rectlist.append(block)

    rectlist.print_list()
    return rectlist

def drawRect(rect):
    left = rect.left
    top = rect.top
    width = rect.width  
    height = rect.height
    # rect_outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left-.5, top - .5, width + .5, height+1))
    rect = pygame.draw.rect(screen, rectangle_color, pygame.Rect(left, top, width, height))

    block = Rect(left, top, width, height)
    block.rect = rect
    # block.outline = rect_outline

    rectlist.append(block)

    # rectlist.insert(rect, index)

def deleteRect(rect): #delete rectangle from pygame canvas
    left = rect.left
    top = rect.top
    width = rect.width  
    height = rect.height
    
    rect = pygame.draw.rect(screen, background_colour, pygame.Rect(left, top, width, height))

def swap_rectangles(rect1, rect2):
    """
        make the rects black
        just switch left and top for rects and draw them again
        also switch order of rectangles in the list
    """
    deleteRect(rect1)
    deleteRect(rect2)

    tmp_w = rect1.width
    tmp_left = rect1.left

    # rect1.width = rect2.width
    rect1.left = rect2.left
    # rect2.width = tmp_w
    rect2.left = tmp_left

    drawRect(rect1)
    drawRect(rect2)

    rect1_index = rectlist.index(rect1)
    rect2_index = rectlist.index(rect2)

    rectlist.list[rect1_index] = rect2
    rectlist.list[rect2_index] = rect1

def shuffle(rectlist):
    #need to shuffle rectangles by randomly swapping them
    length_ = len(rectlist.list)
    for i in range(length_):
        i = random.randint(1, length_)
        j = random.randint(1, length_)
        swap_rectangles(rectlist[i], rectlist[j])

    

    
"""
DEBUG


how do we add 1 to the height for the first rectangle

and need to implement sort still


DEBUG
"""
rectlist = RectList()
draw_rectangles(20)

shuffle(rectlist)



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


