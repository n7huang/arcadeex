import pygame
import random
import sys

#define colours
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

pygame.init()

#set height & width of screen
size = [1000, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("CPT GAME")

#functions!
def button_draw(x,y,menu_check):
    if menu_check == True:
        pygame.draw.rect(screen,RED,[950,550,50,50])
        for button_offset in range (2):
            pygame.draw.rect(screen,RED,[200+button_offset*400,300,200,100])
        if 400 >= x >= 200 and 400 >= y >= 300:
            pygame.draw.rect(screen,GREEN,[200,300,200,100])
        elif 800 >= x >= 600 and 400 >= y >= 300:
            pygame.draw.rect(screen,GREEN,[600,300,200,100])
        elif x >= 950 and y >= 550:
            pygame.draw.rect(screen,GREEN,[950,550,50,50])
    elif menu_check == False:
        pygame.draw.rect(screen,RED,[0,550,50,50])
        if 50 >= x >= 0 and y >= 550:
            pygame.draw.rect(screen,GREEN,[0,550,50,50])

def press_check(x_click,y_click,menu_check):
    if menu_check == True:
        if 400 >= x_click >= 200 and 400 >= y_click >= 300 and menu_check == True:
            print "PLAY TTT"
            return 1
        elif 800 >= x_click >= 600 and 400 >= y_click >= 300 and menu_check == True:
            print "PLAY HM"
            return 2

def exit_check(x,y):
    if menu_check == True:
        if x >= 950 and y >= 550:
            return True
    elif menu_check == False:
        if 50 >= x >= 0 and y >= 550:
            return False

def TTT():
    print "PLAY tic tac toe"

def HM():
    print "PLAY hangman"

def main():
    global menu_check
    start = press_check(mouse_click[0][0],mouse_click[0][1],menu_check)
    button_draw(x_pos,y_pos,menu_check)
    done = exit_check(mouse_click[0][0],mouse_click[0][1])
    if done == True:
        pygame.quit()
        sys.exit()
    elif done == False:
        menu_check = True
    if start == 1:
        screen.fill(WHITE)
        TTT()
        menu_check = False
    elif start == 2:
        screen.fill(WHITE)
        HM()
        menu_check = False

#loop until the user clicks the close button.
done = False
mouse_click = [[-10000,-10000]]
menu_check = True

#Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    #get mouse coordinates
    pos = pygame.mouse.get_pos()
    x_pos = pos[0]
    y_pos = pos[1]

# ----- Main Event Loop -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            done = True
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
            mouse_click.insert(0,[x_pos,y_pos])

    #set the screen background colour
    screen.fill(WHITE)

    main()

    #limit to 30 frames per second
    clock.tick(30)

    #update screen with drawings
    pygame.display.flip()

#idle friendly, anti-hang quit line
pygame.quit()
