# import openai
import pygame
from pygame import mixer
import os
import random
import copy



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
  

pygame.display.set_caption('sort_algo') 

# Fill the background colour to the screen 
screen.fill(background_colour)

sort_complete = False

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

    def __getitem__(self, index):
        return self.list[index]  # Allow indexing like a regular list

    def __setitem__(self, index, value):
        self.list[index] = value  # Allow setting items at an index

    def __repr__(self):
        return f"RectList({self.list})"
    
    def __len__(self):
        return len(self.list)

    def append(self, rect):
        self.list.append(rect)
    
    def print_list(self):
        index = 0
        for block in self.list:
            print("rect " + str(index) + ": " + str(block.left) + " " + str(block.top) + " " + str(block.width) + " " + str(block.height))
            index += 1

    def print_(self, rect):
        index = self.index(rect)
        print("rect " + str(index) + ": " + str(rect.left) + " " + str(rect.top) + " " + str(rect.width) + " " + str(rect.height))

    def index(self, obj):
        index = 0
        for block in self.list:
            if block == obj:
                return index
            index += 1;

    def insert(self, index):
        pass

    
    def shuffle(self):
        #need to shuffle rectangles by randomly swapping them
        length_ = len(self.list)
        for _ in range(length_ * 2):
            i = random.randint(0, length_-1)
            j = random.randint(0, length_-1)
            swap(self.list[i], self.list[j])
        pygame.display.flip()
    
    def shuffle_once(self):
        length_ = int(len(self.list))
        i = random.randint(0, length_-1)
        j = random.randint(0, length_-1)
        print(i, j)
        if i != j:
            swap(self.list[i], self.list[j])
        pygame.display.flip()

def my_range(start, end, increment):
    current_value = start
    values = []
    while current_value < end:
        values.append(current_value)
        current_value += increment
    
    return values

def draw_rectangles(number): 
    divider = int(screen.get_width() / number)
    dividerh = int(screen.get_height() / number)
    # print(screen.get_width(), divider)
    for i in range(0,screen.get_width(),divider): #increment by divider
        left = 0 + i
        top = screen.get_height()-(dividerh*(i / divider))
        width = screen.get_width()/number
        height = screen.get_height()-top
    
        rect_outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left-.5, top - .5, width + .5, height+1))
        rect = pygame.draw.rect(screen, rectangle_color, pygame.Rect(left, top, width-.5, height-.5))

        block = Rect(left, top, width, height)
        block.rect = rect
        # block.outline = rect_outline

        rectlist.append(block)

    # rectlist.print_list()
    print(rectlist)
    pygame.display.update()

def drawRect(rect, color_=None):
    color = (255,255,255)
    if color_ == 'red':
        color = (255,0,0)
    
    left = rect.left
    top = rect.top
    width = rect.width  
    height = rect.height
    rect_outline = pygame.draw.rect(screen, background_colour, pygame.Rect(left-.5, top - .5, width + .5, height+1))
    rect = pygame.draw.rect(screen, color, pygame.Rect(left, top, width-.5, height-.5))

    block = Rect(left, top, width, height)
    block.rect = rect
    # block.outline = rect_outline

  

    # rectlist.insert(rect, index)

def deleteRect(rect): #delete rectangle from pygame canvas
    left = rect.left
    top = rect.top
    width = rect.width  
    height = rect.height
    # rect_outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left-.5, top - .5, width + .5, height+1))

    rect = pygame.draw.rect(screen, background_colour, pygame.Rect(left, top, width-.5, height-.5))
    # rectlist.remove(rect)
    # pygame.time.delay(50)
    pygame.display.update()

def swap(rect1, rect2):
    """
    Swap two rectangles by updating their positions
    and redrawing them properly
    """
    if rect1 == rect2:
        return
    if rect1.left == rect2.left:
        return

    # Store original positions
    rect1_left = rect1.left
    rect2_left = rect2.left
    
    # Clear both rectangles first
    deleteRect(rect1)
    deleteRect(rect2)
    pygame.display.update()  # Update display after deletions
    
    # Update positions
    rect1.left, rect2.left = rect2_left, rect1_left
    
    # Update rectangle objects
   
    
    # Draw the rectangles in their new positions
    drawRect(rect1)
    drawRect(rect2)
    # pygame.display.update()  # Update display after drawing
    
    # Update the positions in the list if needed
    rect1_index = rectlist.index(rect1)
    rect2_index = rectlist.index(rect2)
    rectlist[rect1_index], rectlist[rect2_index] = rect2, rect1
    # pygame.time.delay(50)
    pygame.display.update()


""" algorithms """
def all_sorts():
    pass
def selection_sort(rectlist):
    global sort_complete
    n = len(rectlist)
    for i in range(n-1):
        min_idx = i

        for j in range(i+1, n):
            if rectlist[j].height < rectlist[min_idx].height:
                min_idx = j
        
        swap(rectlist[i], rectlist[min_idx])
    sort_complete = True
def bubble_sort(rectlist):
    global sort_complete
    n = len(rectlist)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if rectlist[j].height > rectlist[j+1].height:
                swap(rectlist[j], rectlist[j+1])
                swapped = False
        if swapped == False:
                break
    sort_complete = True

def insertion_sort(rectlist):
    for i in range(1, len(rectlist)):
        key = rectlist[i]
        j = i-1
        while j >= 0 and key.height < rectlist[j].height:
            swap(rectlist[j+1], rectlist[j])
            j -= 1
        rectlist[j+1] = key

def merge(rectlist, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = rectlist[left + i]
    for j in range(n2):
        R[j] = rectlist[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i].height <= R[j].height:
            swap(rectlist[k], L[i])
            i += 1
        else:
            swap(rectlist[k], R[j])
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        swap(rectlist[k], L[i])
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        swap(rectlist[k], R[j])
        j += 1
        k += 1

def merge_sort_(rectlist, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort_(rectlist, left, mid)
        print("merging left side!")
        merge_sort_(rectlist, mid + 1, right)
        print("merging right side!")
        merge(rectlist, left, mid, right)
        print("merging final 2 sides!")

def merge_sort(rectlist):
    merge_sort_(rectlist, 0, len(rectlist)-1)

""" algorithms """

def animate():
    for rect in rectlist:
        drawRect(rect, 'red')

def check_completion(): #check to see if sorted to play animate
    pass 

def current_block():
    pass #highlight current block
    

    
surface = pygame.display.get_surface()

num_of_rects =600

rectlist = RectList()
draw_rectangles(num_of_rects)


# Update the display using flip 
pygame.display.flip() 

# Variable to keep our game loop running 
running = True

FPS=60
# game loop 
while running: 
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False
    #     elif event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_ESCAPE:
    #             running = False
    #         elif event.key == pygame.K_s:  # Press 'S' to shuffle
    #             rectlist.shuffle()
    #         elif event.key == pygame.K_b:  # Press 'B' to run bubble sort
    #             bubble_sort(rectlist)
    #         elif event.key == pygame.K_i:  # Press 'I' to run insertion sort
    #             insertion_sort(rectlist)

    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                    running = False
    
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
    rectlist.shuffle()

    sorts = [insertion_sort, bubble_sort, selection_sort, merge_sort]
    fast_sorts = [selection_sort, merge_sort]
    
    sort_function = random.choice(fast_sorts)
    sort_function(rectlist)

    # sorts[3](rectlist)

    

        
        
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

DEBUG
"""
