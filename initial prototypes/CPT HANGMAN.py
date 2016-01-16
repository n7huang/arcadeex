import pygame
import random
from pygame.locals import *

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BROWN    = ( 102,  73,   9)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1000, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

rand_number = random.randint(0,19)
wordFile = open('Words.txt','r')
cateFile = open('Cates.txt','r')
wordList = wordFile.readlines()
cateList = cateFile.readlines()
word = wordList[rand_number][:-1]
category = cateList[rand_number][:-1]

line1 = ['A','B','C','D','E','F','G','H','I']
line2 = ['J','K','L','M','N','O','P','Q','R']
line3 = ['S','T','U','V','W','X','Y','Z']
letter_list = []
letter_coords = []
wrong_letterlist = []
correct_letterlist = []

cursor_horiz = 0
cursor_vert = 0
selected_letter = 97
validity = 0
mouse_click = [[-10000,-10000]]

#Drawn objects
def hanger():
    pygame.draw.line(screen, BROWN, [100, 18], [100, 298], 5)
    pygame.draw.line(screen, BROWN, [100, 20], [240, 20], 5)
    pygame.draw.line(screen, BROWN, [240, 18], [240, 90], 5)
    pygame.draw.line(screen, BROWN, [100, 298], [50, 320], 5)
    pygame.draw.line(screen, BROWN, [100, 298], [150, 320], 5)

def lines(line_number):
    for x_offset in range(0,line_number*75,75):
        pygame.draw.line(screen,BLACK,[300+x_offset,300],[350+x_offset,300],5)

def letterbox():
    for x_offset in range(0,630,70):
        for y_offset in range(0,210,70):
            pygame.draw.rect(screen,BLACK,[300+x_offset,390+y_offset,35,35])
    pygame.draw.rect(screen,WHITE,[860,530,35,35])

def highlighter(letter_horiz,letter_vert):
    pygame.draw.rect(screen,RED,[295 + letter_horiz,385 + letter_vert,45,45])

def letters():
    for i in range(0,9):
        font = pygame.font.SysFont('Calibri', 40, True, False)
        text = font.render(line1[i],True,WHITE)
        screen.blit(text, [302+(71 * i), 390])
    for i in range(0,9):
        font = pygame.font.SysFont('Calibri', 40, True, False)
        text = font.render(line2[i],True,WHITE)
        screen.blit(text, [303+(69 * i), 460])
    for i in range(0,8):
        font = pygame.font.SysFont('Calibri', 40, True, False)
        text = font.render(line3[i],True,WHITE)
        screen.blit(text, [303+(69 * i), 530])

def head():
    pygame.draw.ellipse(screen,BLACK,[215,90,50,50],5)
def body():
    pygame.draw.rect(screen,BLACK,[238,140,5,70], 5)
def r_arm():
    pygame.draw.line(screen,BLACK,[240,205],[265,250], 10)
def l_arm():
    pygame.draw.line(screen,BLACK,[240,205],[215,250], 10)
def l_leg():
    pygame.draw.line(screen,BLACK,[240,150],[205,200], 10)
def r_leg():
    pygame.draw.line(screen,BLACK,[240,150],[275,200], 10)

#Drawing functions
def human_drawer():
    if len(wrong_letterlist) >= 1:
        head()
    if len(wrong_letterlist) >= 2:
        body()
    if len(wrong_letterlist) >= 3:
        r_arm()
    if len(wrong_letterlist) >= 4:
        l_arm()
    if len(wrong_letterlist) >= 5:
        r_leg()
    if len(wrong_letterlist) >= 6:
        l_leg()

def cate_drawer():
    font = pygame.font.SysFont('Calibri', 60, True, False)
    text = font.render(category,True,BLACK)
    screen.blit(text, [590, 100])

def letter_drawer(letter,positions):
    for i in range(len(letter_coords)):
        font = pygame.font.SysFont('Calibri', 60, True, False)
        text = font.render(letter,True,BLACK)
        screen.blit(text, [310+(75*positions), 250])

#Logic functions
def incorrect_letters():
    for i in range(len(wrong_letterlist)):
        font = pygame.font.SysFont('Calibri', 60, True, False)
        text = font.render(wrong_letterlist[i],True,BLACK)
        screen.blit(text, [390+(80*i), 320])

def letter_checker():
    no_word = 0
    for i in range(len(word)):
        if chr(selected_letter) == word[i]:
            letter_coords.append([word[i],i])
            correct_letterlist.append(chr(selected_letter))
        else:
            no_word += 1
    if no_word == len(word) and len(wrong_letterlist) < 6:
        wrong_letterlist.append(chr(selected_letter))

#End game functions
def victory():
    pygame.draw.rect(screen,BLACK,[50,325,900,250])
    font = pygame.font.SysFont('Calibri', 70, True, False)
    text = font.render('Congratulations!',True,WHITE)
    screen.blit(text, [250, 325])
    font = pygame.font.SysFont('Calibri', 70, True, False)
    text = font.render('You\'ve won!',True,WHITE)
    screen.blit(text, [300, 425])

def lose():
    pygame.draw.rect(screen,BLACK,[50,325,900,250])
    font = pygame.font.SysFont('Calibri', 70, True, False)
    text = font.render('Sorry! You\'ve lost!',True,WHITE)
    screen.blit(text, [250, 325])
    font = pygame.font.SysFont('Calibri', 70, True, False)
    text = font.render('The word was:',True,WHITE)
    screen.blit(text, [300, 400])
    font = pygame.font.SysFont('Calibri', 70, True, False)
    text = font.render(word,True,WHITE)
    screen.blit(text, [450, 475])

def reset_HM():
    global rand_number,word,category,letter_list,letter_coords,wrong_letterlist,\
    correct_letterlist,cursor_horiz,cursor_vert,selected_letter,validity,no_word
    rand_number = random.randint(0,5)
    word = wordList[rand_number][:-1]
    category = cateList[rand_number][:-1]
    letter_list = []
    letter_coords = []
    wrong_letterlist = []
    correct_letterlist = []
    cursor_horiz = 0
    cursor_vert = 0
    selected_letter = 97
    validity = 0
    no_word = 0

def end_screen(x,y):
     if len(correct_letterlist) == len(word):
        victory()
        pygame.draw.rect(screen,RED,[800,500,50,50])
     elif len(wrong_letterlist) == 6:
        lose()
        pygame.draw.rect(screen,RED,[800,500,50,50])
     if 850 >= x >= 800 and 550 >= y >= 500:
        reset_HM()
        mouse_click.insert(0,[-10000,-10000])

#Main function
def HM():
    hanger()
    human_drawer()
    highlighter(cursor_horiz,cursor_vert)
    cate_drawer()
    letterbox()
    letters()
    lines(len(word))
    for i in range(len(letter_coords)):
        letter_drawer(letter_coords[i][0],letter_coords[i][1])
    incorrect_letters()
    end_screen(mouse_click[0][0],mouse_click[0][1])
    print chr(selected_letter)
    print letter_list
    print wrong_letterlist
    print correct_letterlist
    print word
    print category
    print pos

# -------- Main Program Loop -----------
while not done:
    pos = pygame.mouse.get_pos()
    x_pos = pos[0]
    y_pos = pos[1]

    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if (event.key == K_RIGHT) and cursor_horiz < 560 and selected_letter != 122:
                cursor_horiz += 70
                selected_letter += 1
            elif (event.key == K_LEFT) and cursor_horiz > 0:
                cursor_horiz -= 70
                selected_letter -= 1
            elif (event.key == K_DOWN) and cursor_vert < 140 and selected_letter != 114:
                cursor_vert += 70
                selected_letter += 9
            elif (event.key == K_UP) and cursor_vert > 0:
                cursor_vert -= 70
                selected_letter -= 9
            elif (event.key == K_RETURN):
                for i in range(len(letter_list)):
                    if chr(selected_letter) == letter_list[i]:
                        validity += 1
                if validity == 0:
                    letter_list.append(chr(selected_letter))
                    letter_checker()
                validity = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click.insert(0,[x_pos,y_pos])


    # --- Game logic should go here
    # i.e calculations for positions, variable updates

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # --- Drawing code should go here
    #hang_struc()
    HM()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()


