import pygame
import random

screen = pygame.display.set_mode((1200, 800)) 


background_colour = (0,0,0) 
rectangle_color = (255,255,255) # red baby

merging = False


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

        self.shuffling = False

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
        # print("rect " + str(index) + ": " + str(rect.left) + " " + str(rect.top) + " " + str(rect.width) + " " + str(rect.height))

    def index(self, obj):
        index = 0
        for block in self.list:
            if block == obj:
                return index
            index += 1;

    def insert(self, index):
        pass

    def _shufflingToggle(self):
        self.shuffling = not self.shuffling

    
    def shuffle(self):
        #need to shuffle rectangles by randomly swapping them
        length_ = len(self.list)
        for _ in range(length_ * 2):
            i = random.randint(0, length_-1)
            j = random.randint(0, length_-1)
            self.swap(self.list[i], self.list[j])
            # self.shuffle_once()
        pygame.display.flip()
    
    def shuffle_once(self):
        if self.shuffling:
            length_ = int(len(self.list))
            i = random.randint(0, length_-1)
            j = random.randint(0, length_-1)
            # print(i, j)
            if i != j:
                self.swap(self.list[i], self.list[j])
            pygame.display.flip()

    def draw_rectangles(self, number): 
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

            self.append(block)

        # rectlist.print_list()
        # print(rectlist)
        pygame.display.update()

    def swap(self, rect1, rect2):
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
        rect1_index = self.index(rect1)
        rect2_index = self.index(rect2)
        self[rect1_index], self[rect2_index] = rect2, rect1
        # pygame.time.delay(50)
        pygame.display.update()

def my_range(start, end, increment):
    current_value = start
    values = []
    while current_value < end:
        values.append(current_value)
        current_value += increment
    
    return values



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


def animate(rectlist):
    for rect in rectlist:
        drawRect(rect, 'red')

def check_completion(): #check to see if sorted to play animate
    pass 

def current_block():
    pass #highlight current block

def merging_():
    global merging_
    merging = not merging



def display_text(message, textcolour, bgcolour, screen):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(message, True, textcolour, bgcolour)
    textRect = text.get_rect()
    textRect.center = (40, 40)
    screen.blit(text, textRect)
    return message