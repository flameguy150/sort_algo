# import openai
import pygame
from pygame import mixer
import os
import random
import copy
from utils.algorithms import selection_sort, bubble_sort, merge_sort, insertion_sort
from utils.utilities import Rect, RectList, display_text, display_text_xy, autoplay, check_completion, animate
import time
    

# bubbling = False

pygame.init()
clock = pygame.time.Clock()


song = os.path.join("sounds", "forward.mp3")

mixer.init() 
mixer.music.load(song) 
mixer.music.set_volume(0.7) 
mixer.music.play(-1, 1.0) 

background_colour = (0,0,0) 
rectangle_color = (255,255,255) # red baby
  
screen = pygame.display.set_mode((800, 600)) 
pygame.font.init()
  

pygame.display.set_caption('sort_algo') 

# Fill the background colour to the screen 
screen.fill(background_colour)

sortComplete = False
autoplay_on_ = False #for autoshuffling




    
surface = pygame.display.get_surface()

num_of_rects =400

rectList = RectList(screen)
rectList.create_rectangles(num_of_rects)


# Update the display using flip 
pygame.display.flip() 

# Variable to keep our game loop running 
running = True

sort_generator = None

FPS=60
# game loop 
while running: 
    clock.tick(FPS)

    if sort_generator:
        try:
            next(sort_generator)
        except StopIteration:
            sort_generator = None  # sort finished
        
    if sort_generator:
        sortComplete = False

    if sort_generator == None and not sortComplete:
        if check_completion(rectList):
            animate(rectList) #should only animate after finishing sort, not when resting
            sortComplete = True

    if (autoplay_on_ and not sort_generator):
        sort_generator = autoplay(rectList)
    else:
        rectList.shuffle_once()

    rectList.draw_rectangles()

    #FPS text
    # white = (255,255,255)
    # display_text_xy(str(FPS), white, background_colour, screen, 200, 200)

    
    for event in pygame.event.get():
        # STARTTIME = time.time()
        # time_ = pygame.time.get_ticks()
        # message = "Time: " + str(time_ - STARTTIME) + " milliseconds"
        # display_text(message, rectangle_color, background_colour, screen)
        # pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:  # Press 'r' to shuffle
                sort_generator = rectList._shufflingToggle()    #toggles from true to false
            elif event.key == pygame.K_b:  # Press 'B' to run bubble sort
                sort_generator = bubble_sort(rectList)
            elif event.key == pygame.K_i:  # Press 'I' to run insertion sort
                sort_generator = insertion_sort(rectList)
            elif event.key == pygame.K_m:  # Press 'I' to run insertion sort
                sort_generator = merge_sort(rectList)
            elif event.key == pygame.K_s:  # Press 'I' to run insertion sort
                sort_generator = selection_sort(rectList)
            elif event.key == pygame.K_a:  # Press 'a' to autoplay sorts in random order
                autoplay_on_ = not autoplay_on_
            elif event.key == pygame.K_RETURN: # Press 'Enter' to reset rectangles
                rectList.reset_rectangles()
            elif event.key == pygame.K_UP: #Press '↑' to increase FPS
                if (FPS <= 60):
                    FPS *= 2
                else:
                    FPS += 60
                print(FPS)
            elif event.key == pygame.K_DOWN: #Press '↓' to decrease FPS
                if (FPS <= 60):
                    FPS = FPS / 2
                else:
                    FPS -= 60 
                print(FPS)
    
# print("--- %s seconds ---" % (time.time() - start_time)) 
        
pygame.quit()


"""when sorted, animate coloring
then, loop into another sort

show fps and other cool stuff on top part of screen
cool little expand animation for it?

py -m venv .venv

# 3. Activate (PowerShell)
.\.venv\Scripts\Activate.ps1

"""
