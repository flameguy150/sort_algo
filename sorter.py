# import openai
import pygame
from pygame import mixer
import os
import random
import copy
from algorithms import selection_sort, bubble_sort, merge_sort, insertion_sort
from utilities import Rect, RectList, display_text



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
pygame.init()
clock = pygame.time.Clock()


song = os.path.join("sounds", "forward.mp3")

mixer.init() 
mixer.music.load(song) 
mixer.music.set_volume(0.7) 
mixer.music.play(-1, 1.0) 

background_colour = (0,0,0) 
rectangle_color = (255,255,255) # red baby
  
screen = pygame.display.set_mode((1200, 800)) 
pygame.font.init()
  

pygame.display.set_caption('sort_algo') 

# Fill the background colour to the screen 
screen.fill(background_colour)

sort_complete = False








""" algorithms """


""" algorithms """


    

    
surface = pygame.display.get_surface()

num_of_rects =600

rectList = RectList()
rectList.draw_rectangles(num_of_rects)


# Update the display using flip 
pygame.display.flip() 

# Variable to keep our game loop running 
running = True

FPS=60
# game loop 
while running: 
    time_ = pygame.time.get_ticks()

    message = str(time_)

    display_text(message, rectangle_color, background_colour, screen)
    # if rectlist.shuffling:
    # merge_sort(rectList)
    rectList.shuffle_once()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:  # Press 'r' to shuffle
                rectList._shufflingToggle()    #toggles from true to false
            elif event.key == pygame.K_b:  # Press 'B' to run bubble sort
                bubble_sort(rectList)
            elif event.key == pygame.K_i:  # Press 'I' to run insertion sort
                insertion_sort(rectList)
            elif event.key == pygame.K_m:  # Press 'I' to run insertion sort
                merge_sort(rectList)
            elif event.key == pygame.K_s:  # Press 'I' to run insertion sort
                selection_sort(rectList)

    

    

        
        
pygame.quit()


"""when sorted, animate coloring
then, loop into another sort

show fps and other cool stuff on top part of screen
cool little expand animation for it?

"""
"""
DEBUG
# rectlist[0].top -= 20
# rectlist[0].height += 20
# drawRect(rectlist[0])

# rect1 = rectlist[0]
# rectlist.print_(rect1)
# rect2 = rectlist[18]
# rectlist.print_(rect2)

# rect3 = rectlist[10]
# rect4 = rectlist[19]


# rectlist.print_(rect1)
# rectlist.print_(rect2)
# swap(rect1, rect2)

# rect1 = rectlist[4]
# rect2 = rectlist[5]

# swap(rect1, rect2)

# swap(rect1, rect2)



# for event in pygame.event.get(): 
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_ESCAPE:
    #                 running = False
    
    #     # Check for QUIT event       
    #     if event.type == pygame.QUIT: 
    #         running = False
    # rectlist.shuffle()

    # sorts = [insertion_sort, bubble_sort, selection_sort, merge_sort]
    # fast_sorts = [selection_sort, merge_sort]
    
    # sort_function = random.choice(fast_sorts)
    # sort_function(rectlist)

    # sorts[3](rectlist)

DEBUG
"""
