# import openai
import pygame



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


# pygame.init()

# display_width = 800
# display_height = 600
# gameDisplay = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('Racey')


# pygame.quit()
# quit()

# Define the background colour 
# using RGB color coding. 
background_colour = (234, 212, 252) 
rectangle_color = (255,0,0)
  
# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((800, 400)) 
  
# Set the caption of the screen 
pygame.display.set_caption('algo_sort') 

# Fill the background colour to the screen 
screen.fill(background_colour)

# draw rect on top of screen
# rect1 = pygame.draw.rect(screen, rectangle_color, pygame.Rect(10,10,12,100))
# rect2 = pygame.draw.rect(screen, rectangle_color, pygame.Rect(40,10,12,100))
# rect3 = pygame.draw.rect(screen, rectangle_color, pygame.Rect(10,10,12,110))
# rect4 = pygame.draw.rect(screen, rectangle_color, pygame.Rect(10,10,12,110))
# rect5 = pygame.draw.rect(screen, rectangle_color, pygame.Rect(10,10,12,110))
# rect6 = pygame.draw.rect(screen, rectangle_color, pygame.Rect(10,10,12,110))
# rect7 = pygame.draw.rect(screen, rectangle_color, pygame.Rect(10,10,12,110))
# rect8 = pygame.draw.rect(screen, rectangle_color, pygame.Rect(10,10,12,110))
# rect9 = pygame.draw.rect(screen, rectangle_color, pygame.Rect(10,10,12,110))
# rect10 = pygame.draw.rect(screen, rectangle_color, pygame.Rect(10,10,12,110))




# [10, 1, 9, 5, 6, 3, 2]
# [rect3, rect1, rect2]


# left, top, width and height

def draw_rectangles(number): 
    divider = int(screen.get_width() / number)
    dividerh = int(screen.get_height() / number)
    # print(screen.get_width(), divider)
    for i in range(0,800,divider):
        # outline = rect.inflate(rect.width*2, rect.width*2)
        left = 0 + i
        top = screen.get_height()-(dividerh*(i / divider))
        width = screen.get_width()/number
        height = screen.get_height()-top

        print(left, top, width, height)
    
        rect_outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left-1, top - 1, width + 1, height+2))
        rect = pygame.draw.rect(screen, rectangle_color, pygame.Rect(left, top, width, height))

        # rectangle_array.append(rect)
""""
DEBUG


how do we add 1 to the height for the first rectangle

and need to implement sort still


DEBUG
"""
draw_rectangles(2)



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


