import pygame
import random
from algorithms import merge_sort, selection_sort, insertion_sort, bubble_sort



background_colour = (0,0,0) 
rectangle_color = (255,255,255) # red baby

merging = False




class Rect:
    def __init__(self, screen, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.screen = screen

        self.rect = None
        self.outline = None
        

class RectList:
    def __init__(self, screen):
        self.list = [] # full of rects
        self.screen = screen

        self.shuffling = False
        self.highlight = (-1,-1)
        self.number = 0 #number of rectangles
        

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
            self.draw_rectangles()
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


    def create_rectangles(self, number):
        self.number = number
        self.list.clear()  # clear existing rectangles
        screen = self.screen
        divider = screen.get_width() / number
        dividerh = screen.get_height() / number

        for i in range(number):
            left = i * divider
            height = (i + 1) * dividerh  # or random heights if you want later
            top = screen.get_height() - height
            width = divider

            block = Rect(screen, left, top, width, height)
            self.append(block)
        
    def reset_rectangles(self):
        self.list = []
        self.create_rectangles(self.number)
        self.draw_rectangles()

    def draw_rectangles(self): 
        screen = self.screen
        screen.fill(background_colour)  # clears whole screen

        for idx, rect in enumerate(self.list):
            # black border
            outline_rect = pygame.Rect(rect.left - 0.5, rect.top - 0.5, rect.width + 0.5, rect.height + 1)
            pygame.draw.rect(screen, (0, 0, 0), outline_rect)

            # highlighting
            if idx == self.highlight[0] or idx == self.highlight[1]:
                color = (255, 0, 0)  #red for highlighted rectangles
            else:
                color = (255, 255, 255)  # qhite for normal rectangles

            main_rect = pygame.Rect(rect.left, rect.top, rect.width - 0.5, rect.height - 0.5)
            pygame.draw.rect(screen, color, main_rect)

        pygame.display.update()

    def draw_end(self):
        screen = self.screen
        for rect in (self.list):
            # black border
            outline_rect = pygame.Rect(rect.left - 0.5, rect.top - 0.5, rect.width + 0.5, rect.height + 1)
            pygame.draw.rect(screen, (0, 0, 0), outline_rect)

            # highlighting
            color = (255, 0, 0)

            main_rect = pygame.Rect(rect.left, rect.top, rect.width - 0.5, rect.height - 0.5)
            pygame.draw.rect(screen, color, main_rect)
            pygame.display.update()
            pygame.time.delay(5)

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


        # Update positions
        rect1.left, rect2.left = rect2_left, rect1_left

        # Update rectangle objects
    

        # Draw the rectangles in their new positions
        # drawRect(rect1)
        # drawRect(rect2)
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





def animate(rectlist):
    rectlist.draw_end()

def check_completion(rectlist): #check to see if sorted to play animate
    for i in range(len(rectlist)-1):
        if rectlist[i].height > rectlist[i+1].height: #if this doesn't work, check for height
            return False
    return True

def current_block():
    pass #highlight current block





def display_text(message, textcolour, bgcolour, screen):
    # erase_text(textcolour, bgcolour, screen)
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(message, True, textcolour, bgcolour)
    textRect = text.get_rect()
    textRect.center = (100, 40)
    screen.blit(text, textRect)
    return message

def erase_text(textcolour, bgcolour, screen):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(" ", True, textcolour, bgcolour)
    textRect = text.get_rect()
    textRect.center = (110, 40)
    screen.blit(text, textRect)
    return " "

def display_text_xy(message, textcolour, bgcolour, screen, x, y):
    # erase_text(textcolour, bgcolour, screen)
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(message, True, textcolour, bgcolour)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)
    return message


def autoplay(rectlist):
    rectlist.shuffle()
    sorts = [insertion_sort, bubble_sort, selection_sort, merge_sort]
    i = random.randint(0,3)
    return sorts[i](rectlist)

